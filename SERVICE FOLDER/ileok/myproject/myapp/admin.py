from django.contrib import admin
from .models import NaverMovieData, Sentiword_dict1, Sentiword_dict2 , User_kakao_data
# Register your models here.
admin.site.register(NaverMovieData)
admin.site.register(Sentiword_dict1)
admin.site.register(Sentiword_dict2)
admin.site.register(User_kakao_data)