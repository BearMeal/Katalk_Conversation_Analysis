from asgiref.sync import sync_to_async
from myapp.models import NaverMovieData

'''
import os
import sys

# 프로젝트 루트 경로 설정
project_root = os.path.dirname(os.getcwd())
sys.path.append(project_root)

# 장고 설정 모듈 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 장고 설정 적용
import django
django.setup()

'''


@sync_to_async
def get_data_naver(idx): #idx번째 데이터를 가져온다.
    return NaverMovieData.objects.get(id=idx) 

@sync_to_async
def get_all_data_naver(): #모든 데이터를 가져온다.
    return list(NaverMovieData.objects.all())

