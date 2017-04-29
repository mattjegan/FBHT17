from django.contrib.auth.models import User
from rest_framework import serializers, validators

from api.models import Profile, Mission, Step, Result


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

        # This is gonna be slow as anything but it ain't no time for optimizing now
        completed_missions = []
        results = Result.objects.filter(profile_id=instance.id)
        for mission in Mission.objects.all():
            # Check that all steps in that mission have been completed
            complete = True

            steps = Step.objects.filter(mission=mission)
            if not steps.exists():
                continue

            for step in steps:
                if not results.filter(step=step).exists():
                    complete = False

            if complete:
                completed_missions.append(mission.id)

        ret['completed_missions'] = completed_missions

        return ret

    class Meta:
        model = Profile
        fields = '__all__'


class MissionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(MissionSerializer, self).to_representation(instance=instance)
        steps = Step.objects.filter(mission_id=instance.id)
        ret['steps'] = steps.values_list(flat=True)
        ret['cost'] = sum(steps.values_list('cost', flat=True))
        return ret

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