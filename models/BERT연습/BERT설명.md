## BERT 적용하기위해 알아야하는 RNN계열 모델들과 다른점들 설명

- 텐서플로우에서도 버트를 만들 순 있다. 요런식으로
- ![keras_bert](https://www.tensorflow.org/static/text/tutorials/classify_text_with_bert_files/output_0EmzyHZXKIpm_0.png)
  
- 기존 mecab,okt 형태소 분석기로 토큰화하는게 하지않고, 허깅페이스의 서브워드토크나이저중 하나인 워드피스 토크나이저를 사용해야할듯
- mecab으로 토큰화를 먼저하고 하는 경우도 있는것 같다. 왜그런지 알아보기

- RNN계열에서의 시계열 데이터을 사용하지않고 내부에 ANN 구조가 적용되어 좀더 효율적인듯하다.
