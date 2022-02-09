from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, HashTagViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"product", ProductViewSet, basename="product")
router.register(r"hashtag", HashTagViewSet, basename="hashtag")

urlpatterns = [
] + router.urls