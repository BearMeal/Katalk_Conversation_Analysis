import re
import pickle
import numpy as np
from soynlp.normalizer import repeat_normalize
from transformers import TFAlbertForSequenceClassification
import tensorflow as tf
import random

#참여자 뽑기
def get_user(katok):
    # 중복을 제거하고 참여자 리스트 생성
    user_names = list(set([i[0] for i in katok]))
    return user_names

#두명의 대화를 [[찬란카톡],[하영카톡]]형태로 얻는 함수
def get_convers(user_names,katok):
    received_texts = [
        [j[2] for j in katok if i == j[0]]  ##
        for i in user_names]
    # 이모티콘, 사진, 샵검색 제거 
    exclusion_list = ['사진', '이모티콘', '샵검색:']
    convers_texts = [
    [str(j) for j in i if all(exclusion not in j for exclusion in exclusion_list)]
    for i in received_texts]
    return convers_texts

# 반복,띄어쓰기 정제(Cleaning) 함수
def clean_korean_text(convers_texts):
    convers_texts = re.sub(r'http\S+', '', convers_texts)  #링크를 지운다
    convers_texts = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ\s.!?~^;]', ' ', convers_texts)
    convers_texts = repeat_normalize(convers_texts, num_repeats=2)
    clean_texts = re.sub(r'\s+', ' ', convers_texts).strip()
    return clean_texts

# 입력문장을 정제하고 공백대화를 제거함(https도 같이 없어짐)
# [[찬란카톡],[하영카톡]]가 들어와서 정제하는 함수
def get_clean(convers_texts):
    temp = []
    for convers_text in convers_texts:
        temp.append([ clean_korean_text(i) for i in convers_text if clean_korean_text(i) !='' ]) ##
    clean_texts = temp
    del temp
    return clean_texts

#워드피스 토큰화 적용
def tokenize(clean_texts,tokenizer):
    temp = []
    for clean_text in clean_texts: 
        clean_text = tokenizer(clean_text, truncation=True, padding='max_length', max_length=32,return_token_type_ids= False)
        temp.append(clean_text)
    tokenized_texts = temp
    del temp
    return tokenized_texts

#입력되는 형태 [[찬란토큰화카톡],[하영토큰화카톡]]

#모델예측 [['김찬란',12, 23, 45, 65, 34],['김하영',12, 23, 45, 65, 34]]
#         [[유저1,강부,부정,중성,긍정,강긍],[유저2,강부,부정,중성,긍정,강긍]] 이렇게 출력

def get_prediction(tokenized_texts,loaded_model, user_names,convers_texts):
    predicted = []
    for order,tokenized_text in enumerate(tokenized_texts):
        predictions=loaded_model.predict([
            np.array(tokenized_text['input_ids']),
            np.array(tokenized_text['attention_mask'])
            ])
        counts = [0, 0, 0, 0, 0]
        index_of_strong_nega_texts= []
        index_of_strong_posi_texts= []
        cnt=-1
        for prediction in predictions[0]:
            indices = np.around(tf.nn.softmax(prediction)).astype(int)
            cnt+=1
            #여기서 배열이 다 0이면 컨티뉴 해버린다.
            if len(np.where(indices == 1)[0]) == 0:
                continue
            index = np.where(indices == 1)[0][0]
            counts[index] += 1
            #강부,강긍의 인덱스를저장한다.
            if index == 0:
                index_of_strong_nega_texts.append(cnt)
            if index == 4:
                index_of_strong_posi_texts.append(cnt)
                
        name=user_names[order]
        #4개보다 작을경우 오류 방지
        if len(index_of_strong_nega_texts)>=4:
            strne = random.sample(index_of_strong_nega_texts, 3)
        else :
            strne = index_of_strong_nega_texts
        #해당 인덱스 문장 가져오기
        strne_texts = [ convers_texts[order][i] for i in strne]
            
        if len(index_of_strong_posi_texts)>=4:
            strpo = random.sample(index_of_strong_posi_texts, 3)
        else :
            strpo = index_of_strong_posi_texts
        strpo_texts = [ convers_texts[order][i] for i in strpo]

        #['김찬란',[12, 23, 45, 65, 34],[강한부정들],[강한 긍정들]]
        predicted.append([name, counts, strne_texts, strpo_texts])
        
    return predicted

def load_tokenizer(tokenizer_path):
    with open(tokenizer_path, "rb") as f:
        tokenizer = pickle.load(f)
    return tokenizer

def predict_final(model_path, pklpath, katok):
    # 저장된 모델 불러오기
    loaded_model = TFAlbertForSequenceClassification.from_pretrained(model_path)
    tokenizer=load_tokenizer(pklpath)

    #katok은 이미 get_from_txt처리된 데이터
    user_names = get_user(katok)
    convers_texts = get_convers(user_names,katok)
    clean_texts = get_clean(convers_texts) #안에 clean_korean_text()포함
    tokenized_texts = tokenize(clean_texts,tokenizer)
    predicted=get_prediction(tokenized_texts,loaded_model,user_names,convers_texts)
    return predicted

