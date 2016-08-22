from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from {{ cookiecutter.project_slug }}.api.v1 import serializer as serializers

class CurrentUserView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = serializers.UserSerializer(request.user, data=request.data)
        if request.data and serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
