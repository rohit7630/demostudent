from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer
from rest_framework import status
from django.http import JsonResponse

@api_view(['GET'])
def get_api(request,pk):
           print("hi....................................")
           id= pk
           if id is not None:
                stu = Student.objects.filter(id=id).values()
                print(stu)

                serializer = StudentSerializer(stu)

                #print(serializer)
               #  print("serializerdsdsdssdsdsdsd............................",serializer)
               #  print() 
                return Response(stu[0])
           stu = Student.objects.all()
           serializer = StudentSerializer(stu, many = True)
           return Response(serializer.data)

@api_view(['POST'])    
def post_api(self,request):
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors)
      
@api_view(['PUT'])    
def put_api(self,request,pk):
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu, data = request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Complete Data updated'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])    
def patch_api(self,request,pk):    
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu, data = request.data, partial = True)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Partial Data updated'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors)

@api_view(['DELETE'])    
def delete_api(self,request,pk):
       id = pk
       stu = Student.objects.get(pk=id)
       stu.delete()
       return Response({'msg':'Data Deleted!'})
           
    
