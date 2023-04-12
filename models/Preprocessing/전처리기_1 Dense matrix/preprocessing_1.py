# 모델_1에 들어갈 전처리기 모듈이다.
# db구현전까지는 파일을 불러온다.

from tensorflow.keras.models import *
from tensorflow.keras.layers import *
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np
import pandas as pd
from konlpy.tag import Mecab

train_file = tf.keras.utils.get_file('train.txt', 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt')
train_text = open(train_file,'rb').read().decode(encoding='utf-8')

=> 원시데이터 DB에넣는다.
컬럼 contents, label 두개 df_train 방식처럼해서 들어간다. 

df_train = pd.DataFrame({
    'contents':[ row.split('\t')[1] for row in train_text.split('\n')[1:] if row.count('\t')>0 ],
    'label': [ int(row.split('\t')[2]) for row in train_text.split('\n')[1:] if row.count('\t')>0]
})

=> 여기서 부터 전처리과정 DB에서 불러와서
모듈불러와서 전처리실행


전처리 => X_train_dense = np.expand_dims( X.toarray(), axis=-1 )  #밀집행렬
=> DNN에 학습





#데이터 크기 지정
df_train = df_train[::6]

#문장 추출
texts= [ ]
for i in df_train['feature']:
    texts.append(i)
len(texts)

#문자열이 아닌게 있는지 확인
for i in texts:
    if type(i)!=str:
        print(i)
        
# train 데이터 입력값(X)을 정제(Cleaning)
import re
from soynlp.normalizer import repeat_normalize

def clean_korean_text(text):
    # 특수 문자 및 숫자 제거
    text = re.sub(r'[^가-힣ㄱ-ㅎㅏ-ㅣ\s]', '', text)
    # 반복되는 자음, 모음 제거 (e.g., 'ㅋㅋㅋ' -> 'ㅋ')
    text = repeat_normalize(text, num_repeats=1)
    # 띄어쓰기 정규화 (연속된 공백 문자를 하나의 공백 문자로 변환)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

clean_texts=[]
for i in texts:
    clean_texts.append(clean_korean_text(i))
    
#정제된 텍스트를 벡터화하기전에 토큰화한다

tokenized_clean_texts =[ Mecab(dicpath=r'C:/mecab/mecab-ko-dic').morphs(i) for i in clean_texts ]

rejoined_tokenized_texts = [' '.join(i) for i in tokenized_clean_texts]


vectorizer=TfidfVectorizer( )

X = vectorizer.fit_transform(rejoined_tokenized_texts)
y = df_train.iloc[:,1]

with open('pre_1_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

X_train_dense = np.expand_dims( X.toarray(), axis=-1 )