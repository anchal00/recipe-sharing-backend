from rest_framework import status as http_status
from rest_framework import viewsets
from rest_framework.response import Response

from recipe_app.models import Recipe, User
from recipe_app.serializers import RecipeSerializer, UserSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        if query_params and query_params.get('title'):
            v = query_params.get('title')
            return Recipe.objects.filter(title=query_params.get('title'))
        return Recipe.objects.all()

    def list(self, request):
        return super().list(request)
       
    def retrieve(self, request, pk=None):
        recipe = self.get_object()
        return Response(self.get_serializer(recipe).data)

    def create(self, request):
        if request.user.is_authenticated:
            return super().create(request)
        return Response(status=http_status.HTTP_401_UNAUTHORIZED)
        
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
