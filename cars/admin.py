from django.contrib import admin

from .models import Car
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'doors', 'price_per_day', 'is_available', 'owner')
    list_filter = ('is_available', 'transmission', 'fuel_type', 'doors')
    search_fields = ('brand', 'model', 'description')