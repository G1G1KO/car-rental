from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterPage, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]