import os
from myapp.models import MyModel, User_kakao_data
import numpy as np
# import pickle
# from django.conf import settings
# from konlpy.tag import Okt
import re
# from soynlp.normalizer import repeat_normalize
from datetime import datetime
from model1 import kakao_predict1
from model2 import kakao_predict2
from model3 import kakao_predict3

import concurrent.futures
import asyncio
# from transformers import TFAlbertForSequenceClassification, AlbertTokenizer

def txt_to_numpy_array(file_path):
    if os.path.isfile(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                row = [int(num) for num in line.strip().split(',')]
                data.append(row)
        return np.array(data)
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")

def convert_time_format(korean_time_str):
    korean_time_str = korean_time_str.replace("오전", "AM").replace("오후", "PM")
    try:
        formatted_time = datetime.strptime(korean_time_str, '%p %I:%M').strftime('%H:%M:%S')
        # print(formatted_time + '형식으로 변환 완료')
    except ValueError:
        formatted_time = None
        # print('시간변환실패')
    return formatted_time

def save_data_to_db(sentences):
    for sentence in sentences:
        # 중복 데이터 확인
        duplicate = User_kakao_data.objects.filter(
            sender=sentence[0], content=sentence[2], time=sentence[1]
        ).exists()

        # 중복되지 않은 경우에만 데이터 저장
        if not duplicate:
            user_kakao_data = User_kakao_data(
                sender=sentence[0],
                content=sentence[2],
                time=sentence[1]
            )
            user_kakao_data.save()

def get_from_txt(file):
    data = file.read().decode('utf-8').split('\n')
    sentences = []
    for line in data:
        pattern = r'\[(.*?)\]\s+\[(.*?)\]\s+(.+)'
        match = re.match(pattern, line)
        if match:
            name = match.group(1)  # 첫 번째 대괄호 안의 단어 추출
            time = convert_time_format(match.group(2))  # 두 번째 대괄호 안의 단어 추출 후 시간 변환
            content = match.group(3)  # 대괄호 뒤의 내용 추출
            # print(name, time, content)
            if time is not None:  # 시간 변환이 성공한 경우에만 sentences에 추가
                temp = [name, time, content]
                sentences.append(temp)
    return sentences

def predict_result1(sentences):
    rel_path="../../../finalmodels/model1/"
    
    loaded_model = MyModel('GRU_model_1').load()
    result= kakao_predict1.predict_final(
    loaded_model,
    rel_path+'GRU_tokenizer.pkl',
    sentences)
    return result

def predict_result2(sentences):
    model_path = "../../../finalmodels/model2/albert-kor-base/"
    tokenizer_path="../../../finalmodels/model2/albert-kor-base/albert_tokenizer.pkl"
    
    result= kakao_predict2.predict_final(
        model_path,
        tokenizer_path,
        sentences
    )
    return result

def predict_result3(sentences):
    model_path = "../../../finalmodels/model3/albert-kor-base/"
    tokenizer_path="../../../finalmodels/model3/albert-kor-base/albert_tokenizer.pkl"
    
    result= kakao_predict3.predict_final(
        model_path,
        tokenizer_path,
        sentences
    )
    return result

# def predict_models(uploaded_file):
#     sentences = get_from_txt(uploaded_file)  # 텍스트 파일에서 데이터 추출
#     print('***get_from_txt 완료***')
#     # save_data_to_db(sentences)  # 추출된 데이터를 DB에 저장
#     # print('***save_data_to_db 완료***')
#     # result1 = predict_result1(sentences)  # 딥러닝 모델 호출 및 결과 예측
#     # print('***model1 OK***')
#     # print(result1)
#     # result2 = predict_result2(sentences)  # 딥러닝 모델2 호출 및 결과 예측
#     # print('***model2 OK***')
#     # print(result2)
#     # result3 = predict_result3(sentences)  # 딥러닝 모델2 호출 및 결과 예측
#     # print('***model3 OK***')
#     # print(result3)

#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future1 = executor.submit(predict_result1, sentences)
#         future2 = executor.submit(predict_result2, sentences)
#         future3 = executor.submit(predict_result3, sentences)
#     result1 = future1.result()
#     result2 = future2.result()
#     result3 = future3.result()

#     return result1, result2, result3

async def predict_models(uploaded_file):
    sentences = get_from_txt(uploaded_file)
    loop = asyncio.get_running_loop()
    future1 = loop.run_in_executor(None, predict_result1, sentences)
    future2 = loop.run_in_executor(None, predict_result2, sentences)
    future3 = loop.run_in_executor(None, predict_result3, sentences)
    result_list = await asyncio.gather(future1, future2, future3)
    return tuple(result_list)