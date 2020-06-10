from django.shortcuts import render, get_object_or_404,Http404
from django.contrib.auth.models import User
from notice.models import Notice
from notice.serializers import NoticeSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class NoticeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    startswith_title = filters.CharFilter(field_name='title', method='filter_title')

    def filter_title(self, queryset, title, value):
        title_filter = {f'{title}__startswith': value}

        return queryset.filter(**title_filter)

    class Meta :
        model = Notice
        fields = ('price',)


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NoticeFilter


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


