from ..models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class UserViewSet(viewsets.ViewSet):
#
#     def get_user(self, pk):
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist as exc:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         return user
#
#     def list(self, request, format=None):
#         try:
#             queryset = User.objects.all()
#         except User.DoesNotExist as exc:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def create(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None, format=None):
#         user = self.get_user(pk)
#         serializer = UserSerializer(instance=user)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def update(self, request, pk=None, format=None):
#         user = self.get_user(pk)
#         serializer = UserSerializer(instance=user, data=request.data)
#
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as exc:
#             return Response(data=serializer.errors, exception=exc, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#     def partial_update(self, request, pk=None, format=None):
#         user = self.get_user(pk)
#         serializer = UserSerializer(instance=user, data=request.data, partial=True)
#
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as exc:
#             return Response(data=serializer.errors, exception=exc, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#     def destroy(self, request, pk=None, format=None):
#         user = self.get_user(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
