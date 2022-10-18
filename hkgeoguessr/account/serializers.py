from rest_framework import serializers
from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        depth = 0
        fields = [
            'uid',
            'username',
            'answered',
            'avatar_url',
            'rating',
            'is_staff',
            'is_superuser',
            'is_active',
            'email',
            'date_joined',
            'last_login',
        ]
        read_only_fields = [
            'id',
            'answered',
            'rating',
            'date_joined',
            'last_login',
        ]
