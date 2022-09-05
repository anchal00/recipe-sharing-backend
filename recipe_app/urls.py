from rest_framework.routers import DefaultRouter

from recipe_app.apis import RecipeViewSet

router = DefaultRouter()
router.register(prefix=r'recipes', viewset=RecipeViewSet, basename='recipe')
urlpatterns = router.urls
