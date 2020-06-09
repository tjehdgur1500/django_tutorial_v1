from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notice import views

urlpatterns = [
    path('notice/', views.NoticeList.as_view()),
    path('notice/<int:pk>/', views.NoticeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)