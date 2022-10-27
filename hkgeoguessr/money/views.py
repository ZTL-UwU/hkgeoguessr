from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hkgeoguessr.tools import (check_ans, update_rating)

from .serializers import MoneySerializer
from money.models import Money
from account.models import Account


class MoneyView(APIView):

    # Get problem content
    def get(self, request, pid):
        money = get_object_or_404(Money, pid=pid)

        serializer = MoneySerializer(money)
        return Response({'res': serializer.data}, status=status.HTTP_200_OK)

    # Add new problem
    def post(self, request):
        data = request.data

        serializer = MoneySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class MoneyAnswerView(APIView):

    # Answer a problem
    def post(self, request, pid):
        money = get_object_or_404(Money, pid=pid)
        user = get_object_or_404(Account, request.user.uid)

        update_rating(user, problem=money, O=check_ans(
            request.data['end_geo'], money.start_geo, money.end_geo))

        return Response(status=status.HTTP_201_CREATED)
