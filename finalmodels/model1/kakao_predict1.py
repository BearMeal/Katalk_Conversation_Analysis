import re
import pickle
from konlpy.tag import Okt
from soynlp.normalizer import repeat_normalize
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# 카톡대화 불러와서 정제,(정규화코드)하는 함수
# def get_from_txt(txt):
#     data= open(txt,"r", encoding='utf-8').read().split('\n')
#     sentences=[]
#     for line in data:
#         pattern = r'\[(.*?)\]\s+\[(.*?)\]\s+(.+)'
#         match = re.match(pattern, line)
#         if match:
#             name = match.group(1)  # 첫 번째 대괄호 안의 단어 추출
#             time = match.group(2)  # 두 번째 대괄호 안의 단어 추출
#             content = match.group(3)  # 대괄호 뒤의 내용 추출
#             # print(name, time, content)
#             temp=[name,time,content]
#             sentences.append(temp)    
#     return sentences

#참여자 뽑기
def get_user(katok):
    # 중복을 제거하고 참여자 리스트 생성
    user_names = list(set([i[0] for i in katok]))
    return user_names


#두명의 대화를 [[찬란카톡],[하영카톡]]형태로 얻는 함수
def get_convers(user_names,katok):
    received_texts = [
        [j[2] for j in katok if i == j[0]]
        for i in user_names]
    # 이모티콘, 사진, 샵검색 제거 
    exclusion_list = ['사진', '이모티콘', '샵검색:']
    preclean_texts = [
    [str(j) for j in i if all(exclusion not in j for exclusion in exclusion_list)]
    for i in received_texts]
    return preclean_texts

# 텍스트 특수문자, 반복,띄어쓰기 정제(Cleaning) 함수
def clean_korean_text(preclean_texts):
    preclean_texts = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ\s]', ' ', preclean_texts)
    preclean_texts = repeat_normalize(preclean_texts, num_repeats=1)
    clean_texts = re.sub(r'\s+', ' ', preclean_texts).strip()
    return clean_texts

# 입력문장을 정제하고 공백대화를 제거함(https도 같이 없어짐)
# [[찬란카톡],[하영카톡]]가 들어와서 정제하는 함수
def get_clean(convers_texts):
    temp = []
    for i in convers_texts:
        temp.append([ clean_korean_text(j) for j in i if clean_korean_text(j) !='' ])
    clean_texts = temp
    del temp
    return clean_texts

#형태소 분리
def get_morphs(clean_text):
    okt= Okt()
    temp1 =[]
    for sentences in clean_text:
        temp2 = []
        for sent in sentences:
            temp2.append(okt.morphs(sent))
        temp1.append(temp2)
    morphs_text =temp1
    del temp1
    return morphs_text

#벡터화
def get_vectorizer(loaded_tokenizer, morphs_text):
    temp=[]
    for i in morphs_text:
        test_sequences = loaded_tokenizer.texts_to_sequences(i)
        #길이 제한은 모델학습할떄의 max_length
        paded_sequences = pad_sequences(test_sequences,padding='post',maxlen=23) 
        temp.append(paded_sequences)  
    vetorized_text=temp
    del temp
    return vetorized_text

#모델예측 [['김찬란',123,34],['김하영',234,547]]  [[유저1,부정,긍정],[유저2,부정,긍정]]
def get_predict(loaded_model,vetorized_text,user_names):
    predicted =[]
    for order,sequence in enumerate(vetorized_text):
        prediction = loaded_model.predict(sequence)  
        cnt0=0; cnt1=0 
        for i in prediction.squeeze().tolist():
            if i < 0.5:  #부정이면
                cnt0+=1
            else :    #긍정이면 
                cnt1+=1
        name=user_names[order] 
        predicted.append([name,cnt0,cnt1])
    return predicted
        
# katok=get_from_txt('./sample.txt')

def predict_final(loaded_model, pklpath, katok):
    # 저장된 모델 불러오기
    loaded_model= loaded_model

    #저장된 vectorizer 불러오기
    with open(pklpath, 'rb') as f:
        loaded_tokenizer = pickle.load(f)

    user_names=get_user(katok)
    convers_texts = get_convers(user_names,katok)
    clean_text = get_clean(convers_texts)
    morphs_text = get_morphs(clean_text)
    vetorized_text =get_vectorizer(loaded_tokenizer, morphs_text)
    predicted= get_predict(loaded_model, vetorized_text,user_names)
    print(predicted)
    return predicted

