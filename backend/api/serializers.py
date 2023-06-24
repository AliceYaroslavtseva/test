from rest_framework import serializers

from statement.models import RequestMessage, Request


class RequestMessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        fields = '__all__'
        model = RequestMessage


class RequestSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        model = Request
        fields = '__all__'
