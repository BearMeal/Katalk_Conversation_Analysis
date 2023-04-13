## Attention에대한 간단한 설명
- 양방향 LSTM모델 이후 중요한 데이터에 더욱 가중치를 줄수있도록 
- seq2seq 구조의 모델에서 decoder에서 encoder로 qurley를 key값을 참조하면서 attention에서 score를 매기고 softmax를 적용한 가중치를 FCL층으로 보내어 다시 decoder와 이러쿵해서 출력레이어로 보낸다.  
- 이후 RNN을 이용하지않고 인코더,디코더를 만든것이 transmer이다. 변역을 위해 만들어 졌지만 문맥을 파악하여 다양한 감정분류에 효과적으로 사용할수 있을것이다. => 최적은 아니다.

- Attention이 여러종류가있다.