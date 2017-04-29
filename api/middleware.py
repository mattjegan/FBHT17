
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from api.models import Mission

class ExpiryMiddleware(MiddlewareMixin):
    """
    This should DEFINITELY be a celery task but I cbb setting up a celery queue on heroku right now
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Expire any missions needing expiry
        Mission.objects.filter(expire__lt=datetime.now()).update(active=False)

        response = self.get_response(request)

        return response