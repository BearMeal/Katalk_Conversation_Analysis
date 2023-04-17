from asgiref.sync import sync_to_async
from myapp.models import NaverMovieData, Sentiword_dict1, Sentiword_dict2, User_kakao_data

'''
# 필수실행
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
#create
@sync_to_async 
def create_data_naver(content, label):
    naver = NaverMovieData(content=content, label=label)
    naver.save()
#read
@sync_to_async
def get_data_naver(idx): #idx번째 데이터를 가져온다.
    return NaverMovieData.objects.get(id=idx) 
#read all
@sync_to_async
def get_all_data_naver(): #모든 데이터를 가져온다.
    return list(NaverMovieData.objects.all())
#delete
@sync_to_async
def delete_data_naver(idx): #idx번째 데이터를 가져온다.
    naver = NaverMovieData.objects.get(id=idx)
    naver.delete()
###############################################################

#create
@sync_to_async 
def create_data_senti1(content, label):
    senti1 = Sentiword_dict1(content=content, label=label)
    senti1.save()
#read
@sync_to_async
def get_data_senti1(idx): #idx번째 데이터를 가져온다.
    return Sentiword_dict1.objects.get(id=idx) 
#read all
@sync_to_async
def get_all_data_senti1(): #모든 데이터를 가져온다.
    return list(Sentiword_dict1.objects.all())
#delete
@sync_to_async
def delete_data_senti1(idx): #idx번째 데이터를 가져온다.
    senti1 = Sentiword_dict1.objects.get(id=idx)
    senti1.delete()
###############################################################

#create
@sync_to_async 
def create_data_senti2(content, sentiment, frequency, degree1, degree2):
    senti2 = Sentiword_dict2(content=content, sentiment=sentiment, frequency=frequency, degree1=degree1, degree2=degree2)
    senti2.save()
#read
@sync_to_async
def get_data_senti2(idx): #idx번째 데이터를 가져온다.
    return Sentiword_dict2.objects.get(id=idx) 
#read all
@sync_to_async
def get_all_data_senti2(): #모든 데이터를 가져온다.
    return list(Sentiword_dict2.objects.all())
#delete
@sync_to_async
def delete_data_senti2(idx): #idx번째 데이터를 가져온다.
    senti2 = Sentiword_dict2.objects.get(id=idx)
    senti2.delete()
###############################################################

#create
@sync_to_async 
def create_data_kakao(sender, content, time):
    kakao = User_kakao_data(sender=sender, content=content, time=time)
    kakao.save()
#read
@sync_to_async
def get_data_kakao(idx): #idx번째 데이터를 가져온다.
    return User_kakao_data.objects.get(id=idx) 
#read all
@sync_to_async
def get_all_data_kakao(): #모든 데이터를 가져온다.
    return list(User_kakao_data.objects.all())
#delete
@sync_to_async
def delete_data_kakao(idx): #idx번째 데이터를 가져온다.
    kakao = User_kakao_data.objects.get(id=idx)
    kakao.delete()