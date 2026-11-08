from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"