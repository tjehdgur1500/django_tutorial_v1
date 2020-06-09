from django.shortcuts import render
from notice.models import Notice
from notice.serializers import NoticeSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
# Create your views here.
