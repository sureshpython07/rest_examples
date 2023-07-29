from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_api.models import Student,Post
from rest_api.serializers import StudentSerializer,PostSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
# Create your views here.
# Start Functin based api views this fuction for get list of resource and create resource. 
@csrf_exempt
def student_list_fbv(request):
    if request.method=='GET':
        stud=Student.objects.all()
        serializer=StudentSerializer(stud,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='POST':
        data=JSONParser().parse(request)
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=404)
# Functin based api views this class for get single row of resource,update,delete resource. 
@csrf_exempt
def student_detail_fbv(request,id):
    try:
        get_stud=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return JsonResponse({'msg':'Not Available'},status=404)
    if request.method=='GET':
        serilizer=StudentSerializer(get_stud)
        return JsonResponse(serilizer.data,status=status.HTTP_200_OK)
    elif request.method =='PUT':
        data=JSONParser().parse(request)
        serializer=StudentSerializer(get_stud,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        get_stud.delete()
        return JsonResponse({'msg':'deleted successfully'},status=status.HTTP_200_OK)
    return JsonResponse(status=404)

# here using api_view decorators
@api_view(['GET','POST']) 
def stud_list_fbv_api_view(request):
    if request.method=='GET':
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def stud_detail_fbv_api_view(request,pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'msg':'Resource is not available'},status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        student.delete()
        return Response({'msg':'deleted successfully'},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
# end function based views using api_view() decorators

# start class based api views
class Std__List_CBV(APIView):
    def get(self,request,*args, **kwargs):
        student=Student.objects.all()
        if student is not None:
            serializer=StudentSerializer(student,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self,request,*args, **kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class Std_detail_CBV(APIView):
    def get_std_by_id(self,id):
        try:
            student=Student.objects.get(id=id)
            return student
        except Student.DoesNotExist:
            return None
    def get(self,request,id,*args, **kwargs):
        student=self.get_std_by_id(id)
        if student is None:
            return Response({'msg':'Resource is not existing'})
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,id,*args, **kwargs):
        student=self.get_std_by_id(id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id,*args, **kwargs):
        student=self.get_std_by_id(id)
        student.delete()
        return Response({'msg':'Resource deleted successfully'},status=status.HTTP_202_ACCEPTED)
 # end class based view 

# Start Mixin and generic class based view 
class Std_mixin_gen_CBV_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]
    #lookup_field='id'
    def get(self,request,*args, **kwargs):
            return self.list(request,*args, **kwargs)
    def post(self,request):
        return self.create(request)
    
class Std_mixin_gen_CBV_detail(generics.GenericAPIView,
                               mixins.UpdateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    #lookup_field='id'
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
# Using generic class-based views
class Std_gen_list(generics.ListCreateAPIView):
    serializer_class=Student
    queryset=Student.objects.all()
class Std_gen_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Student
    queryset = Student.objects.all()


# start viewsets and routers
class StudentViewSet_list(viewsets.ViewSet):
    def list(self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class StudentViewSet_detail(viewsets.ViewSet):
    def retrieve(self,request,pk):
        qs=Student.objects.all()
        student= get_object_or_404(qs,pk=pk)
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def update(self,request,pk):
        pass
    def destroy(self,request,pk):
        pass
# generic viewset
class Std_Generic_ViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()

