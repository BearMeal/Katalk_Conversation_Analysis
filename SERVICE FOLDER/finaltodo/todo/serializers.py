from .models import Todo
from rest_framework import serializers

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=[
            'id',
            'title',
            'complete',
            'important',
        ]

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=[
            'id',
            'title',
            'description',
            'created',
            'complete',
            'important',
        ]

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=[
            
            'title',
            'description',
            
            
            'important',
        ]