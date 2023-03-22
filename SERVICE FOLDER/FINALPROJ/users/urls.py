from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)