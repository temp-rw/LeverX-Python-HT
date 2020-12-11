from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import User


class UserBaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        name = request.META.get('HTTP_USERNAME')
        password = (request.META.get('HTTP_PASSWORD'))
        if not name:
            return None

        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)