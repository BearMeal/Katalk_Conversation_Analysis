## 전처리기 개요- 23.04.12
1. 메캅토큰화 => TF-IDF 벡터화 => 모델1의 DNN, 모델2의 SVM에 적용되었음
   
2. 메캅토큰화 => 시계열 데이터(시퀀스) => RNN계열(lstm, gru, attention) 모델에 모두 적용
   
3. 메캅토큰화 => word2vec계열(skipgram,cbow,glove,fasttext)등 사전학습모델을 통해 (이 프로젝트에서는fasttext를 사용하며 직접 학습시켜본다. ) 벡터화(시퀀스데이터)
=> RNN모델에 모두 적용해본다.

### 서브워드임베딩방식
- 서브워드임베딩 방식
4. 허깅페이스의 워드피스 => BERT모델에 적용

### fasttext와 wordpiece tokenizer를 하는이유
- 모델2, 3에서 학습데이터가 다중클래스 분류가 되면서 기존의 방식으로는 OOV(out-of-vocabory)의 학습되지않은 데이터로 인해 성능이 매우 낮아져서 이를 보완할수있는 방식인 ngram을 통해 oov문제해결에 접근하는 fasttext와, 
원래 단어를 분할하여 서브워드를 방식으로 학습하여 oov문제해결에 접근하는 wordpiece 방법을 사용해 볼것이다. 