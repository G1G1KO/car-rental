from django.utils import timezone
from .models import Rental

def release_expired_rentals():
    now = timezone.now()

    expired_rentals = Rental.objects.filter(
        end_date__lte=now,
        car__is_available=False
    )

    for rental in expired_rentals:
        car = rental.car
        car.is_available = True
        car.save(update_fields=['is_available'])
        
        if hasattr(rental, 'is_active'):
            rental.is_active = False
            rental.save(update_fields=['is_active'])