
# from api.models import Mission
#
# class ExpiryMiddleware(object):
#     """
#     This should DEFINITELY be a celery task but I cbb setting up a celery queue on heroku right now
#     """
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         # Expire any missions needing expiry
#         Mission.objects.filter(expire=)
#
#         response = self.get_response(request)
#
#         return response