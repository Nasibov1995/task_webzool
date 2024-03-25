from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    user_email = serializers.SerializerMethodField()

    def get_user_email(self, obj):
        return obj.user_id.email

    class Meta:
        model = Products
        fields = '__all__'
        




