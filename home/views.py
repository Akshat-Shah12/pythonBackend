from functools import partial
from django.db.models import manager
from django.shortcuts import render

#Imported this
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .serializers import *
from .models import *
### We dont have to return a page( We have to return a json Data)
# def hom(request):
#     return render(request,"home.html"),

@api_view(['GET'])
def hello_world(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs,many=True)
    return Response({'status':200,"all_data": serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,"error":serializer.errors,"message": "something went wrong"})

    serializer.save()
    print(data)
    return Response({'status':200,"data":serializer.data,"message":"Working"})
    
@api_view(['PATCH'])
def update_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj,data=request.data,partial=True)
        if not serializer.is_valid():
            return Response({'status':403,"error":serializer.errors,"message": "invalid input"})

        serializer.save()
        # print(data)
        return Response({'status':200,"data":serializer.data,"message":"Working"})
    except Exception as e:
        return Response({'status':404,"message":"Incorrect id"})

    
@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        # print(data)
        return Response({'status':200,"message":"Deleted"})
    except Exception as e:
        return Response({'status':404,"message":"Incorrect id"})