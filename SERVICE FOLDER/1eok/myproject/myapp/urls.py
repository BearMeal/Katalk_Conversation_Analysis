from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('detail/', views.detail, name='detail'),
]