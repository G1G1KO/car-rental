from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect




# Create your views here.

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