# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import mixins


class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,req,*args, **kwargs):
        return self.list(req, *args, **kwargs)
    def post(self,req,*args, **kwargs):
        return self.create(req, *args, **kwargs)
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field='bid'

    def get(self,req,*args, **kwargs):
        return self.retrieve(req, *args, **kwargs)
    def put(self,req,*args, **kwargs):
        return self.update(req, *args, **kwargs)
    def delete(self,req,*args, **kwargs):
        return self.destroy(req, *args, **kwargs)

#이 상태에서 수정, 삭제 추가 

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

class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'


from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

