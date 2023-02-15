from rest_framework.views import APIView

# # class socialApi(APIView):
# #     def get(self,request):
# #         pass 
# #     def post(self,request):
# #         pass 

# #     def put(self,request):
# #         pass 
# #     def patch(self,request):
# #         pass 
# #     def delete(self,request):
# #         pass 

# from django.shortcuts import render 
# from rest_framework.decorators import api_view

# from rest_framework import Response
from apps.users.serializers  import UserCreateSerializer
# # def home (request):

# # return render(request, 'home.html)
# from rest_framework.authentication import TokenAuthentication 
# from rest_framework.permissions import IsAuthenticated 
# from rest_framework_simplejwt.authentication import JWTAuthentication

# class djoserAPI (APIView):

#     authentication_classes =[JWTAuthentication] 
#     permission_classes =[IsAuthenticated]

#     def get(self, request):

#         CustomUser_objs = CustomUser.objects.all() 
#         serializer = UserCreateSerializer(CustomUser_objs, many=True)

#         print(request.user) 
#         return Response({'status':200,'payload': serializer.data})

#     def post(self, request):
#         serializer = UserCreateSerializer(data = request.data)

#         if not serializer.is_valid() :
#             print(serializer.errors)

#         return Response({'status':200,'error':serializer.error,'message':'Somthin wrong'})

from rest_framework.authtoken.models import Token
from rest_framework import generics
from apps.users.models import CustomUser


class UserGeneric(generics.ListAPIView,generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer