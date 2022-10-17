from rest_framework import serializers
from problem.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['pid', 'video_link', 'rating', 'start_geo', 'end_geo']
        depth = 0
        extra_kwargs = {'end_geo': {'write_only': True}}
