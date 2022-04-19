from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.SimpleRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("/api/v1/", include(router.urls)),
]
