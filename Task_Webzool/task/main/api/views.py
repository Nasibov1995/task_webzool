from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,ListAPIView,GenericAPIView
from main.models import *
from main.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser




class ListProductApi(ListAPIView):
    queryset = Products.objects.filter(status=True).order_by("-id")
    serializer_class = ProductSerializer
    
    
class CreateProductApi(GenericAPIView):
    serializer_class = ProductSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductIdApi(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductDetailAPI(RetrieveAPIView):
    queryset = Products.objects.filter(status=True)
    serializer_class = ProductSerializer


class ListCreateCommentApi(ListCreateAPIView):
    queryset = Comments.objects.all().order_by("-id")
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs["pk"]
        return Comments.objects.filter(prod_id=product_id)
