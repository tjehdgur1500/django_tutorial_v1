from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from notice import views


router = routers.SimpleRouter()
router.register(r'notice', views.NoticeViewSet, basename='notice')
urlpatterns = router.urls
