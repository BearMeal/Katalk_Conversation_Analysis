from django.urls import path
from .views import *

urlpatterns = [
    path('todo/',TodosAPIView.as_view()),
    path('todo/<int:id>',TodoAPIView.as_view()),
    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:id>', DoneTodoAPIView.as_view()),    
]

