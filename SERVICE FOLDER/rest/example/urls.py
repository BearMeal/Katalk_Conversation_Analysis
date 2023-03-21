from django.urls import path
from .views import HelloAPI, BookAPI, BooksAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path('books/',BooksAPI.as_view()),
    path('book/<int:bid>/',BookAPI.as_view()),
]
