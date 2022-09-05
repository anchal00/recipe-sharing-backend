from rest_framework import serializers, viewsets
from rest_framework.response import Response

from recipe_app.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


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
