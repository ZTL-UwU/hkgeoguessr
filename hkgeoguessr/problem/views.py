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

        ps = ProblemSerializer(problem)
        return Response({'res': ps.data}, status=status.HTTP_200_OK)

    # Add new problem
    def post(self, request):
        data = request.data

        ps = ProblemSerializer(data=data)
        ps.is_valid(raise_exception=True)
        ps.save()

        return Response(status=status.HTTP_201_CREATED)


class ProblemAnswerView(APIView):

    # Answer a problem
    def post(self, request, pid):
        problem = get_object_or_404(Problem, pid=pid)
        user = get_object_or_404(Account, uid=request.data['uid'])

        update_rating(user, problem=problem, O=check_ans(
            request.data['end_geo'], problem.start_geo, problem.end_geo))

        return Response(status=status.HTTP_201_CREATED)
