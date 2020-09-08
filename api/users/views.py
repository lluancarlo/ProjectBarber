from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """ViewSet to add a customer"""

    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    def list(self, request):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            user_detail = User.objects.get(pk=pk, is_active=True)
        except User.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        user_detail.is_active = False
        user_detail.save()
        return Response(status=HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
