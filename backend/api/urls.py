from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import RequestViewSet, RequestMessageViewSet

router_v1 = DefaultRouter()
router_v1.register('request', RequestViewSet)
router_v1.register(r'request/(?P<request_id>\d+)/massages',
                   RequestMessageViewSet, basename='massages')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
