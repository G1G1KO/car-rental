from .utils import release_expired_rentals

class ExpiredRentalsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        release_expired_rentals()
        return self.get_response(request)