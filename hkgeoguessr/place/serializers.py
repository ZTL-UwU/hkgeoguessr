from rest_framework import serializers
from place.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['pid', 'pic_link', 'rating', 'answered', 'pos_x', 'pos_y']
        depth = 0
        extra_kwargs = {'pos_x': {'write_only': True},
                        'pos_y': {'write_only': True}}
