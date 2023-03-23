from django.urls import path
from . import views


urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('new/', views.photo_new, name='photo_new'),
    path('<int:pk>/', views.photo_detail ,name='photo_detail'),
    path('<int:pk>/edit/', views.photo_edit ,name='photo_edit'),
]
