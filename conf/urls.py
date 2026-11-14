from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from cars.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('cars/', include('cars.urls')),
]
