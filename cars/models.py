from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Car(models.Model):
    TRANSMISSION_CHOICES = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    )

    FUEL_CHOICES = (
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
    )

    CITY_CHOICES = [
        ('tbilisi', 'თბილისი'),
        ('batumi', 'ბათუმი'),
        ('kutaisi', 'ქუთაისი'),
        ('rustavi', 'რუსთავი'),
        ('gori', 'გორი'),
        ('zugdidi', 'ზუგდიდი'),
        ('poti', 'ფოთი'),
        ('telavi', 'თელავი'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    doors = models.PositiveIntegerField(default=4)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, default='automatic')
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, default='gasoline')
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(
        max_length=50,
        choices=CITY_CHOICES,
        default='tbilisi',
    )

    likes = models.ManyToManyField(User, related_name='liked_cars', blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals')
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    days = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk and not self.end_date:
            self.end_date = timezone.now() + timedelta(days=self.days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.car} - {self.renter.username} ({self.days} day)"