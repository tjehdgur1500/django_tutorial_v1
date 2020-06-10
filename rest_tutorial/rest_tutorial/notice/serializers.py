from rest_framework import serializers
from notice.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        # fields 를 __all__ 로 모든필드를 json 으로 response 해줄수 있지만
        # 치명적인 정보 (user 의 정보나 암호)를 보내기떄문에 사용을 지양해야함

