from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from api.models import Profile, Mission, Step, Result, CompleteReceipt
from api.serializers import ProfileSerializer, MissionSerializer, StepSerializer, ResultSerializer, ImageSerializer

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
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('author', 'active',)

    def get_queryset(self):
        qs = super(MissionList, self).get_queryset()

        # Filter based on current_user to have just the missions that are incomplete
        current_user = self.request.query_params.get('current_user', None)

        if current_user is None:
            return qs

        profile = Profile.objects.filter(pk=current_user)
        if not profile.exists():
            return qs

        profile = profile.first()
        return qs.exclude(pk__in=list(profile.completed_missions))


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

        if response.status_code >= 200 and response.status_code < 300:
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


class UploadImage(APIView, ):

    def post(self, request, *args, **kwargs):

        # Create the image
        image = ImageSerializer(data=request.data)
        if not image.is_valid():
            return Response(image.errors, status=400)

        image.save()
        return Response(image.to_representation(image.instance), status=200)
