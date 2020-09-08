from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    url(r"", include(router.urls)),
]
