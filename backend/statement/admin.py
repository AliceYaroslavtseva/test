from django.contrib.admin import ModelAdmin, register

from statement.models import (Request, RequestMessage)


@register(Request)
class RequestAdmin(ModelAdmin):
    list_display = ('id', 'user', 'theme', 'phone_number')
    search_fields = ('id',)


@register(RequestMessage)
class RequestMessageAdmin(ModelAdmin):
    list_display = ('id', 'user', 'message', 'request')
