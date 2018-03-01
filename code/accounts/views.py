from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

class UserApiView(APIView):
    authentication_classes = (TokenAuthentication, )
    # authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': request.user.username,  # `django.contrib.auth.User` instance.
            'auth': request.auth.key,
        }
        return Response(content)


class GenToken(APIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        pass