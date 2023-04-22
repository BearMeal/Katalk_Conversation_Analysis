import os
from myapp.models import MyModel, User_kakao_data
import numpy as np
import pickle
from django.conf import settings
from konlpy.tag import Okt
import re
from soynlp.normalizer import repeat_normalize
from datetime import datetime
from model1 import kakao_predict1
from model2 import kakao_predict2
from model3 import kakao_predict3
from transformers import TFAlbertForSequenceClassification, AlbertTokenizer



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

# def predict_result(txt_file):    
#     model = MyModel("100millon_model").load()
#     txt_file2 = txt_to_numpy_array(txt_file)
#     result = model.predict(txt_file2)
    
#     return result



# def predict_result2(txt_file): #텍스트 파일을 전처리 -> 결과 출력까지 하는 메서드
#     def clean_korean_text(text):
#         # 특수 문자 및 숫자 제거
#         text = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ\s]', '', text)
#         # 반복되는 자음, 모음 제거 (e.g., 'ㅋㅋㅋ' -> 'ㅋ')
#         text = repeat_normalize(text, num_repeats=1)
#         # 띄어쓰기 정규화 (연속된 공백 문자를 하나의 공백 문자로 변환)
#         text = re.sub(r'\s+', ' ', text).strip()
#         return text

#     def get_from_txt(txt):
#         data= open(txt,"r", encoding='utf-8').read().split('\n')
#         sentences=[]
#         for line in data:
#             pattern = r'\[(.*?)\]\s+\[(.*?)\]\s+(.+)'
#             match = re.match(pattern, line)
#             if match:
#                 name = match.group(1)  # 첫 번째 대괄호 안의 단어 추출
#                 time = match.group(2)  # 두 번째 대괄호 안의 단어 추출
#                 content = match.group(3)  # 대괄호 뒤의 내용 추출
#                 # print(name, time, content)
#                 temp=[name,time,content]
#                 sentences.append(temp)    
#         return sentences
    
#     def load_vectorizer(name):
#         model_path = os.path.join(settings.MODEL_DIR, f"{name}.pkl")
#         with open(model_path, "rb") as f:
#             vectorizer = pickle.load(f)
#         return vectorizer

#     loaded_model = MyModel("model1").load()
#     loaded_test_vectorizer=load_vectorizer('vectorizer2')
#     target_name = '김하영' #김하영으로 한정해놓고 일단 구현
#     received_texts= []
#     for i in get_from_txt(txt_file): 
#         if i[0] == target_name:
#             received_texts.append( i[2] )
            
#     # 이모티콘, 사진, 샵검색 제거 
#     clean1_received_texts = []
#     for i in received_texts:
#         if '샵검색:' not in i: 
#             if "이모티콘" not in i:
#                 if '샵검색:' not in i:
#                     clean1_received_texts.append(str(i))

#     clean2_received_texts= [clean_korean_text(i) for i in clean1_received_texts]

#     # 불러온 벡터라이저로 테스트 데이터 변환
#     X_received_texts = loaded_test_vectorizer.transform(clean2_received_texts)
#     X_received_texts_dense = X_received_texts.toarray()


#     # 불러온 모델을 사용하여 예측 수행
#     predictions = np.round(loaded_model.predict(X_received_texts_dense))
    
#     return predictions
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

'''
def get_from_txt(file):
    data = file.read().decode('utf-8').split('\n')
    sentences = []
    for line in data:
        pattern = r'\[(.*?)\]\s+\[(.*?)\]\s+(.+)'
        match = re.match(pattern, line)
        if match:
            name = match.group(1)  # 첫 번째 대괄호 안의 단어 추출
            time = match.group(2)  # 두 번째 대괄호 안의 단어 추출
            content = match.group(3)  # 대괄호 뒤의 내용 추출
            # print(name, time, content)
            temp = [name, time, content]
            sentences.append(temp)
    return sentences

'''
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

# def predict_result2(sentences):
    
#     def load_vectorizer(name):
#         model_path = os.path.join(settings.MODEL_DIR, f"{name}.pkl")
#         with open(model_path, "rb") as f:
#             vectorizer = pickle.load(f)
#         return vectorizer
    
#     def clean_korean_text(text):
#         # 특수 문자 및 숫자 제거
#         text = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ\s]', '', text)
#         # 반복되는 자음, 모음 제거 (e.g., 'ㅋㅋㅋ' -> 'ㅋ')
#         text = repeat_normalize(text, num_repeats=1)
#         # 띄어쓰기 정규화 (연속된 공백 문자를 하나의 공백 문자로 변환)
#         text = re.sub(r'\s+', ' ', text).strip()
#         return text

#     target_name = '김하영'
#     loaded_model = MyModel("model2").load()
#     loaded_vectorizer = load_vectorizer('model2')
#     print('***load_vectorizer 완료***')

#     received_texts = []
    
#     for i in sentences:
#         if i[0] == target_name:
#             received_texts.append(i[2])
#             print('***{} 발견 성공***'.format(target_name))
#         else:
#             print('***{} 발견 실패***'.format(target_name))
            
#     # 이모티콘, 사진, 샵검색 제거 
#     clean1_received_texts = []
#     for i in received_texts:
#         if '샵검색:' not in i: 
#             if "이모티콘" not in i:
#                 if '샵검색:' not in i:
#                     clean1_received_texts.append(str(i))

#     clean2_received_texts= [clean_korean_text(i) for i in clean1_received_texts]

#     #정제된 텍스트를 벡터화하기전에 토큰화한다
#     tokenized_clean_test_texts =[ Okt().morphs(i) for i in clean2_received_texts ]
#     tokenized_clean_test_texts

#     #토큰화된걸 ' ' 공백한칸을 기준으로 다시 합쳐준다.
#     rejoined_tokenized_test_texts = [' '.join(i) for i in tokenized_clean_test_texts]
#     rejoined_tokenized_test_texts

#     # 불러온 벡터라이저로 테스트 데이터 변환
#     X_received_texts = loaded_vectorizer.transform(rejoined_tokenized_test_texts)
#     X_received_texts_dense = X_received_texts.toarray()


#     # 불러온 모델을 사용하여 예측 수행
#     predictions = np.round(loaded_model.predict(X_received_texts_dense))
#     print(type(predictions))

#     return predictions

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
