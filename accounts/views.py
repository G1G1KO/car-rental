from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages
from django.shortcuts import redirect

from cars.models import Car, Rental


# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_cars'] = Car.objects.filter(owner=user).order_by('-created_at')
        context['liked_cars'] = Car.objects.filter(likes=user)
        context['rentals'] = Rental.objects.filter(renter=user, is_active=True).order_by('-start_date')
        return context


class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')  

    def form_valid(self, form):
        form.save()

        messages.success(self.request, "Registration Completed successfully")

        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('cars:list-cars')
        return super().get(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('cars:list-cars')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('cars:list-cars')
        return super().get(request, *args, **kwargs)