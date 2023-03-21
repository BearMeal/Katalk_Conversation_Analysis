from django import forms
from .models import App1

class PhotoForm(forms.ModelForm):
    class Meta:
        model=App1
        fields=(
            'title',
            'author',
            'image',
            'description',
            'price',
        )