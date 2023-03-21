# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer



# 함수형 
# @api_view(['GET'])
# def HelloAPI(req):
#     return Response('hello world')

#클래스형
class HelloAPI(APIView):
    def get(self, req):
        return Response('hello world')
    
class BooksAPI(APIView):
    def get(self, req):
        books=Book.objects.all()
        serializer=BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,req):
        serializer=BookSerializer(data= req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView):
    def get(self, req, bid):
        book=get_object_or_404(Book, bid=bid)
        serializer=BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)