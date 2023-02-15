# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework import status
# from ..api_app.serializers import FileSerializer


# class FileView(APIView):
#   parser_classes = (MultiPartParser, FormParser)

#   def post(self, request, *args, **kwargs):
#     file_serializer = FileSerializer(data=request.data)
#     if file_serializer.is_valid():
#       file_serializer.save()
#       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# #  insert this file data into the DB 
# def insert(self, request):
    
    
#     file=codecs.EncodedFile(request.FILES.get("file").open(),"utf-8")
#     reader = pd.read_csv(file, delimiter=";")
#     reader.columns = ['title','author','datetime'];
#     size=int(reader.shape[0])+1
#     index = pd.RangeIndex(start=1, stop=size, step=1, name="no_record")
#     reader_index= reader.set_index(index)
#     print("Dataframe reader_index=",reader_index)
    
#     reader_json=reader.to_json(orient = 'records')
#     print(reader_json)
#     #serializer = DataSourceSerializer(data=)



from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api_app.serializers import UserCreateSerializer, UserLoginSerializer
from apps.api_app.models import User


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        # if not serializer.is_valid():
        #     raise ValidationError(serializer.errors)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
