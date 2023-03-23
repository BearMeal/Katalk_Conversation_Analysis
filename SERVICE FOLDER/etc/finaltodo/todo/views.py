from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer

from rest_framework.generics import get_object_or_404
# Create your views here.

class TodosAPIView(APIView):
    def get(self,request):
        todos=Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class TodoAPIView(APIView):
    def get(self,request, id):
        todo=get_object_or_404(Todo, id=id)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, id):
        todo=get_object_or_404(Todo, id=id)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones=Todo.objects.filter(complete=True)
        serializer=TodoSimpleSerializer(dones,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoneTodoAPIView(APIView):
    def get(self, request, id):
        done=get_object_or_404(Todo, id=id)
        done.complete = True
        done.save()
        serializer=TodoDetailSerializer(done)
        return Response(status=status.HTTP_200_OK)