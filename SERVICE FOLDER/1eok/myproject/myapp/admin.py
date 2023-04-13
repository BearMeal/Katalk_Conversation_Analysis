from django.contrib import admin
from .models import UploadedFile
from .models import NaverMovieData
from .models import Product
# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(NaverMovieData)
admin.site.register(Product)