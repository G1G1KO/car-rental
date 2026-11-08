from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Car


class CarList(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'cars/list_car.html'
    context_object_name = 'cars'
    ordering = ['-created_at']
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = context['cars'].filter(is_available=True)        
        return context


class CarDetail(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'cars/detail_car.html'
    context_object_name = 'car'


class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['brand', 'model', 'year', 'price_per_day', 'doors', 'transmission', 'fuel_type', 'description']
    template_name = 'cars/create_car.html'
    success_url = reverse_lazy('cars:list-cars')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    template_name = 'cars/update_car.html'
    fields = ['brand', 'model', 'year', 'price_per_day', 'doors', 'transmission', 'fuel_type', 'description']
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