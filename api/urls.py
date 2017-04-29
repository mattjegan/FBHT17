from django.conf.urls import include, url

urlpatterns = [
    url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'steps/'),
    # url(r'steps/(?P<step_id>[0-9]+)/'),
    # url(r'missions/'),
    # url(r'missions/(?P<mission_id>[0-9]+)/'),
    # url(r'profiles/'),
    # url(r'profiles/(?P<profile_id>[0-9]+)/'),
    # url(r'results/'),
    # url(r'results/(?P<result_id>[0-9]+)/'),
]