import os
from myapp.models import MyModel, User_kakao_data
import numpy as np
import re
from datetime import datetime
from model1 import kakao_predict1
from model2 import kakao_predict2
from model3 import kakao_predict3
import asyncio


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
    return formatted_time

def save_data_to_db(sentences):
    for sentence in sentences:
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
            name = match.group(1) 
            time = convert_time_format(match.group(2))  
            content = match.group(3)  
            # print(name, time, content)
            if time is not None:  
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

async def predict_models(uploaded_file):
    sentences = get_from_txt(uploaded_file)
    # save_data_to_db(sentences)
    loop = asyncio.get_running_loop()
    future1 = loop.run_in_executor(None, predict_result1, sentences)
    future2 = loop.run_in_executor(None, predict_result2, sentences)
    future3 = loop.run_in_executor(None, predict_result3, sentences)
    result_list = await asyncio.gather(future1, future2, future3)
    return tuple(result_list)