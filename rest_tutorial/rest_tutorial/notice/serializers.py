from rest_framework import serializers
from notice.models import Notice, LANGUAGE_CHOICE, STYLE_CHOICE


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

