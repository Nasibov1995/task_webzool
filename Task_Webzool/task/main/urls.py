from django.urls import path
from main.api import views


urlpatterns = [
    
    
    path("", views.ListProductApi.as_view()),
    path("create_product/", views.CreateProductApi.as_view()),
    path("product_detail/<int:pk>", views.ProductDetailAPI.as_view()),
    path("product_detail/<int:pk>/comments", views.ListCreateCommentApi.as_view()),
    path("products/<int:pk>/", views.ProductIdApi.as_view()),
    
    
]
