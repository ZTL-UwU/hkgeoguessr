from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hkgeoguessr.tools import (check_ans_place, update_rating)

from .serializers import PlaceSerializer
from .models import Place
from account.models import Account


class PlaceView(APIView):

    # Get problem content
    def get(self, request, pid):
        place = get_object_or_404(Place, pid=pid)

        serializer = PlaceSerializer(place)
        return Response({'res': serializer.data}, status=status.HTTP_200_OK)

    # Add new problem
    def post(self, request):
        data = request.data

        serializer = PlaceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class PlaceAnswerView(APIView):

    # Answer a problem
    def post(self, request, pid):
        place = get_object_or_404(Place, pid=pid)
        user = get_object_or_404(Account, request.user.uid)

        update_rating(user, problem=place, O=check_ans_place(
            request.data['pos_x'], request.data['pos_y'], place.pos_x, place.pos_y))

        return Response(status=status.HTTP_201_CREATED)
