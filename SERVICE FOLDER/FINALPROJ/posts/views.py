from rest_framework import viewsets, permissions

from users.models import Profile
from .models import Post
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes=[CustomReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author = self.request.user, profile=profile)
