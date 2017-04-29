import io
import os

import editdistance
from google.cloud import vision
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, validators

from api.models import Profile, Mission, Step, Result, CompleteReceipt, Image


class ProfileSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(allow_blank=False, allow_null=False,
                                   validators=[validators.UniqueValidator(User.objects.all())])
    password = serializers.CharField(max_length=1000, allow_blank=False, allow_null=False)
    first_name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)

    def to_representation(self, instance):
        ret = super(ProfileSerializer, self).to_representation(instance=instance)
        missions = Mission.objects.filter(author_id=instance.id)
        ret['expired_missions'] = missions.filter(active=False).values_list(flat=True)
        ret['active_missions'] = missions.filter(active=True).values_list(flat=True)
        ret['completed_missions'] = CompleteReceipt.objects.filter(profile_id=instance.id).values_list(flat=True) #completed_missions

        return ret

    class Meta:
        model = Profile
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(MissionSerializer, self).to_representation(instance=instance)
        steps = Step.objects.filter(mission_id=instance.id)
        ret['steps'] = steps.values_list(flat=True)
        ret['cost'] = instance.cost
        return ret

    class Meta:
        model = Mission
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):

    step = serializers.PrimaryKeyRelatedField(queryset=Step.objects.all())
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    content = serializers.CharField(allow_blank=False, allow_null=False)

    def validate_content(self, value):

        if value.startswith('http'):
            try:
                # Instantiates a client
                vision_client = vision.Client()

                # Create the image request
                image = vision_client.image(source_uri=value)

                # Performs landmark detection on the image file
                landmarks = image.detect_landmarks(limit=10)

                # Get the landmark values to match against
                print('Landmarks:')
                match_values = []
                for landmark in landmarks:
                    print(landmark.description)
                    match_values.extend(landmark.description.split(' '))

                # Get the comparison values from the Step
                step_id = self.initial_data.get('step', None)
                if step_id is None:
                    raise serializers.ValidationError('Can not do image recognition without \'step\' field')
                step = Step.objects.get(id=step_id)
                comparison_values = []
                comparison_values.extend(step.name.split(' '))
                comparison_values.extend(step.desc.split(' '))

                print('Match Values: {}'.format(match_values))
                print('Compa Values: {}'.format(comparison_values))

                # Do the comparison
                match = False
                for mval in match_values:
                    for cval in comparison_values:
                        if editdistance.eval(mval.lower(), cval.lower()) <= 2:
                            match = True
                            break
                    if match:
                        break

                if not match:
                    raise serializers.ValidationError('Unverifiable Image')

            except serializers.ValidationError as ve:
                raise ve
            except Exception as e:
                return value

        return value



    class Meta:
        model = Result
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer, ):

    image = Base64ImageField(required=False)

    class Meta:
        model = Image
        fields = '__all__'
