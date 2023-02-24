from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class StudentAPI(APIView):
    def get(self,request,format = None,pk=None):
        if request.method =='GET':
        id=pk
        print('..........................',id)



        # if id is not None:
        #     query = Student.objects.filter(id=id)
        #     serializer =StudentSerializer(query)
        #     return Response(serializer.data)
        # query = Student.objects.all()
        # serializer = StudentSerializer(query,many=True)
        # return Response(serializer.errors)
    
    def post_api(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def put_api(self,pk,request, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Complete Data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch_api(self, pk, request, format = None):
       id = pk
       stu = Student.objects.get(pk=id)
       serializer = StudentSerializer(stu,data =request.data, partial = True)
       if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Partial Data updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete_api(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Msg':'Deleted Data'})
    
        


