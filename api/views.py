from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from api.models import Profile, Mission, Step, Result
from api.serializers import ProfileSerializer, MissionSerializer, StepSerializer, ResultSerializer

class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MissionList(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetail(RetrieveAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class StepList(ListCreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class StepDetail(RetrieveAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer


class ResultList(ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetail(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer