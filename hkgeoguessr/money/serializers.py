from rest_framework import serializers
from money.models import Money


class MoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = ['pid', 'video_link', 'rating', 'answered', 'start_geo', 'end_geo']
        depth = 0
        extra_kwargs = {'end_geo': {'write_only': True}}
