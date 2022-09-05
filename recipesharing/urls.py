from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipe_app.urls')),
    path('api/token', TokenObtainPairView.as_view(), name="jwt_token_obtain"),
    path('api/token/refresh', TokenRefreshView.as_view(), name='jwt_token_refresh')
]
