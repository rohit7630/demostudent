from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status



@api_view(['GET'])
def get_api(request): 
       print('..................................',request.data)      
       emp = Employee.objects.filter(emp_id= request.data['id'])
       serializer = EmployeeSerializer(emp, many = True)
       return Response(serializer.data)

@api_view(['POST'])    
def post_api(request):
       serializer = EmployeeSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors)


@api_view(['PUT'])    
def put_api(request,pk):
       id = pk
       stu = Employee.objects.get(pk=id)
       serializer = EmployeeSerializer(stu, data = request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Complete Data updated'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])    
def patch_api(request,pk):    
       id = pk
       stu = Employee.objects.get(pk=id)
       serializer = EmployeeSerializer(stu, data = request.data, partial = True)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Partial Data updated'}, status=status.HTTP_201_CREATED)
       return Response(serializer.errors)

@api_view(['DELETE'])    
def delete_api(request,pk):
       id = pk
       stu = Employee.objects.get(pk=id)
       stu.delete()
       return Response({'msg':'Data Deleted!'})



