from dataclasses import fields
from rest_framework import viewsets
from models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'posted_by', 'recipe_body', 'created_at', 'updated_at']