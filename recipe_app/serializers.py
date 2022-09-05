from rest_framework import serializers

from recipe_app.models import Recipe, User


class RecipeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    posted_by = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']