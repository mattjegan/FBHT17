from django.conf.urls import include, url
from api.views import ProfileList, ProfileDetail, MissionList, MissionDetail, \
    StepList, StepDetail, ResultList, ResultDetail, LoginView, UploadImage

urlpatterns = [
    url(r'login/$', LoginView.as_view()),
    url(r'profiles/$', ProfileList.as_view()),
    url(r'profiles/(?P<pk>[0-9]+)/$', ProfileDetail.as_view()),
    url(r'missions/$', MissionList.as_view()),
    url(r'missions/(?P<pk>[0-9]+)/$', MissionDetail.as_view()),
    url(r'steps/$', StepList.as_view()),
    url(r'steps/(?P<pk>[0-9]+)/$', StepDetail.as_view()),
    url(r'results/$', ResultList.as_view()),
    url(r'results/(?P<pk>[0-9]+)/$', ResultDetail.as_view()),
    url(r'upload/$', UploadImage.as_view()),
]