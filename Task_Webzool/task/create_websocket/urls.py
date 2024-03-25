from django.urls import path
from main.api import views
from .routing import websocket_urlpatterns

urlpatterns = [
    path("product_detail/<int:pk>/comments", views.ListCreateCommentApi.as_view()),
    # Other DRF URLs...
]

# Add WebSocket URL patterns
urlpatterns += websocket_urlpatterns
