from rest_framework import serializers
from place.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['pid', 'pic_link', 'rating', 'answered', 'pos']
        depth = 0
        extra_kwargs = {'pos': {'write_only': True}}
