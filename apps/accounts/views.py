from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
import re
from accounts.validators import PhoneNumberValidator
from django.core.exceptions import ValidationError

class SigUpView(APIView):
    def perform_authentication(self, request):
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request, *args, **kwargs):
        email = self.request.data.get("email")
        phone_number = self.request.data.get("phone_number")
        password = self.request.data.get("password")
        
        try:
            if len(password) < 8:
                raise ValidationError(message="글자수 확인")
        except Exception as e:
            print(e.__dict__)    
            
        User.objects.create(
            email=email,
            password=password,
            phone_number=phone_number
        )
        
        
        
        
        
        return Response(status=status.HTTP_200_OK)

