from rest_framework.routers import DefaultRouter

from recipe_app.apis import RecipeViewSet, UserViewSet

router = DefaultRouter()

router.register(prefix=r'recipes', viewset=RecipeViewSet, basename='recipe')
router.register(prefix=r'users', viewset=UserViewSet, basename='user')

urlpatterns = router.urls
