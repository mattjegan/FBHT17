from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from api.models import Profile, Mission, Step, Result, CompleteReceipt
from api.serializers import ProfileSerializer, MissionSerializer, StepSerializer, ResultSerializer

class LoginView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        # Check we have the fields we need
        if not (email and password):
            return Response({
                'detail': 'Both email and password is required'
            }, status=400)

        # Verify them
        profile = Profile.objects.filter(email=email, password=password)
        if profile.exists():
            return Response({
                'detail': 'Success'
            }, status=200)

        return Response({
            'detail': 'Failed'
        }, status=400)


class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class MissionList(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionDetail(RetrieveUpdateDestroyAPIView):
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

    def create(self, request, *args, **kwargs):
        # Create the result as usual
        response = super(ResultList, self).create(request, *args, **kwargs)

        # If it completed a mission, pay the profile
        step_id = response.data.get('step')
        profile_id = response.data.get('profile')
        profile = Profile.objects.get(id=profile_id)
        mission = Step.objects.get(id=step_id).mission

        results = Result.objects.filter(step__mission=mission, profile_id=profile_id)
        if results.count() == Step.objects.filter(mission=mission).count():
            # Complete!
            complete_receipt = CompleteReceipt(profile=profile, mission=mission)
            complete_receipt.save()

            # Pay the user
            profile.amount += mission.cost
            profile.save()

        return response


class ResultDetail(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer