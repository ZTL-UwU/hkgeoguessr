from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from hkgeoguessr.tools import (check_ans, update_rating)

from .serializers import ProblemSerializer
from problem.models import Problem
from account.models import Account


class ProblemView(APIView):

    # Get problem content
    def get(self, request, pid):
        problem = get_object_or_404(Problem, pid=pid)

        serializer = ProblemSerializer(problem)
        return Response({'res': serializer.data}, status=status.HTTP_200_OK)

    # Add new problem
    def post(self, request):
        data = request.data

        serializer = ProblemSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class ProblemAnswerView(APIView):

    # Answer a problem
    def post(self, request, pid):
        problem = get_object_or_404(Problem, pid=pid)
        user = get_object_or_404(Account, uid=request.data['uid'])

        update_rating(user, problem=problem, O=check_ans(
            request.data['end_geo'], problem.start_geo, problem.end_geo))

        return Response(status=status.HTTP_201_CREATED)
