from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from statement.models import Request, RequestMessage

from .serializers import RequestMessageSerializer, RequestSerializer


class RequestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestMessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = RequestMessageSerializer

    def get_queryset(self):
        request = get_object_or_404(Request, pk=self.kwargs.get('request_id'))
        queryset = RequestMessage.objects.filter(request=request).order_by("id")
        return queryset

    def perform_create(self, serializer):
        request = get_object_or_404(Request, pk=self.kwargs.get('request_id'))
        serializer.save(user=self.request.user, request=request)
