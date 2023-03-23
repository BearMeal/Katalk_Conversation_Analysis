# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('hello/', HelloAPI),
#     path('books/',BooksAPI.as_view()),
#     path('book/<int:bid>/',BookAPI.as_view()),
#     path('mixin/books/',BooksAPIGenerics.as_view()),
#     path('mixin/book/<int:bid>/',BookAPIGenerics.as_view()),
# ]

from rest_framework import routers
from .views import BookViewSet

router= routers.SimpleRouter()
router.register('books',BookViewSet)

urlpatterns=router.urls
