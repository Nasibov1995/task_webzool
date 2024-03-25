from django.urls import re_path
from .consumers import CommentConsumer

websocket_urlpatterns = [
    re_path(r'product_detail/(?P<pk>\d+)/comments/$', CommentConsumer.as_asgi()),
]
