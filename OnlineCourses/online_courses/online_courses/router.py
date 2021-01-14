from courses.api.viewsets import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
urlpatterns = router.urls
