from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarList.as_view(), name='list-cars'),
    path('<int:pk>/', views.CarDetail.as_view(), name='car-detail'),
    path('add/', views.CarCreate.as_view(), name='car-create'),
    path('<int:pk>/edit/', views.CarUpdate.as_view(), name='car-update'),
    path('<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'), 
    path('<int:pk>/like/', views.CarLikeToggleView.as_view(), name='car-like'),
    path('<int:pk>/rent/', views.RentCar.as_view(), name='car-rent'),
]