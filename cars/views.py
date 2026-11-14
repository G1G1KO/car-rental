from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.db.models import Q

from .models import Car, Rental


class RentCar(LoginRequiredMixin, View):
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)

        if not car.is_available or car.owner == request.user:
            return redirect('cars:car-detail', pk=car.pk)
        try:
            days = int(request.POST.get('days', 1))
        except (ValueError, TypeError):
            days = 1      

        if days < 1:
            days = 1 

        total_price = car.price_per_day * days

        Rental.objects.create(
            car=car,
            renter=request.user,
            days=days,
            total_price=total_price
        )
        car.is_available = False
        car.save()
        return redirect('accounts:profile')


class CarLikeToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        if request.user in car.likes.all():
            car.likes.remove(request.user)
        else:
            car.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER', 'cars:list-cars'))


class HomeView(TemplateView):
    template_name = 'cars/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        available_cars = Car.objects.filter(is_available=True)

        context['top_cars'] = available_cars.annotate(
            likes_count = Count('likes')
        ).order_by('-likes_count', '-created_at')[:5]

        context['latest_cars'] = available_cars.order_by('-created_at')[:5]

        return context
    

class CarList(ListView):
    model = Car
    template_name = 'cars/list_car.html'
    context_object_name = 'cars'
    ordering = ['-created_at']
         
    def get_queryset(self):
        queryset =  super().get_queryset().filter(is_available=True)

        search_query = self.request.GET.get('search', '').strip()
        city = self.request.GET.get('city','')
        fuel = self.request.GET.get('fuel', '')
        transmission = self.request.GET.get('transmission', '')
        max_price = self.request.GET.get('max_price', '')

        if search_query:
            queryset = queryset.filter(
                Q(brand__icontains=search_query) | Q(model__icontains=search_query)
            )

        if city:
            queryset = queryset.filter(city=city)

        if fuel:
            queryset = queryset.filter(fuel_type=fuel)

        if transmission:
            queryset = queryset.filter(transmission=transmission)

        if max_price:
            queryset = queryset.filter(price_per_day__lte=max_price)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_choices'] = Car.CITY_CHOICES
        context['fuel_choices'] = Car.FUEL_CHOICES
        context['transmission_choices'] = Car.TRANSMISSION_CHOICES
        return context


class CarDetail(DetailView):
    model = Car
    template_name = 'cars/detail_car.html'
    context_object_name = 'car'


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['brand', 'model', 'year', 'city', 'price_per_day', 'doors', 'transmission', 'fuel_type', 'description']
    template_name = 'cars/create_car.html'
    success_url = reverse_lazy('cars:list-cars')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    template_name = 'cars/update_car.html'
    fields = ['brand', 'model', 'year', 'city', 'price_per_day', 'doors', 'transmission', 'fuel_type', 'description']
    success_url = reverse_lazy('cars:list-cars')

    def test_func(self):
        # ამოწმებს, არის თუ არა შესული მომხმარებელი ამ მანქანის პატრონი
        car = self.get_object()
        return self.request.user == car.owner


class CarDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    template_name = 'cars/delete_car.html'
    context_object_name = 'car'
    success_url = reverse_lazy('cars:list-cars')

    def test_func(self):
        # ამოწმებს, არის თუ არა შესული მომხმარებელი ამ მანქანის პატრონი
        car = self.get_object()
        return self.request.user == car.owner