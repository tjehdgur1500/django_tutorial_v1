# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from snippets import views
#
#
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)