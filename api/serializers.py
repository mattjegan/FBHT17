from django.contrib.auth.models import User
from rest_framework import serializers, validators

from api.models import Profile, Mission, Step, Result


class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(allow_blank=False, allow_null=False,
                                   validators=[validators.UniqueValidator(User.objects.all())])
    password = serializers.CharField(max_length=1000, allow_blank=False, allow_null=False)
    first_name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)

    class Meta:
        model = Profile
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'