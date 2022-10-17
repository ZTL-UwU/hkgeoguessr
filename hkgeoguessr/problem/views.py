from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProblemSerializer
from problem.models import Problem


class ProblemView(APIView):

    def get(self, request, pid):
        problem = get_object_or_404(Problem, pid=pid)

        ps = ProblemSerializer(problem)
        return Response({'res': ps.data}, status=status.HTTP_200_OK)
