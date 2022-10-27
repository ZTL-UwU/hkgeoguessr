from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from django.contrib import auth

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer
from hkgeoguessr.tools import is_email


class AccountView(APIView):
    # Get account data
    def get(self, request, uid):
        account = get_object_or_404(Account, uid=uid)

        serializer = AccountSerializer(account)
        return Response({'res': serializer.data}, status=status.HTTP_200_OK)

    # Create new account
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not is_email(email):
            return Response({'detail': 'Email is not correct'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Account.objects.create_user(
                username=username, password=password, email=email)
        except IntegrityError:
            # failed, probably because username already exits
            return Response({'detail': 'Failed to create user.'}, status=status.HTTP_409_CONFLICT)

        if user:  # Success
            user.save()

            return Response(
                {'detail': 'Success', 'res': {'id': user.id}},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({'detail': 'Failed to create user.'}, status=status.HTTP_409_CONFLICT)


class AccountSessionView(APIView):

    # Login
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)

            return Response(
                {'detail': 'Success', 'res': {'id': user.id}},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {'detail': 'Username or password wrong'},
                status=status.HTTP_403_FORBIDDEN,
            )

    # Logout
    def delete(self, request):

        if not request.user.is_authenticated:
            return Response({'detail': 'Not logged in'}, status=status.HTTP_401_UNAUTHORIZED)

        auth.logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
