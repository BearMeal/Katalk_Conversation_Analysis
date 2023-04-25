
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import predict_result1, predict_result2, predict_result3, get_from_txt, save_data_to_db

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file= request.FILES['file']
            sentences = get_from_txt(uploaded_file)  # 텍스트 파일에서 데이터 추출
            print('***get_from_txt 완료***')
            save_data_to_db(sentences)  # 추출된 데이터를 DB에 저장
            print('***save_data_to_db 완료***')
            result = predict_result1(sentences)  # 딥러닝 모델 호출 및 결과 예측
            print('***model1 OK***')
            print(result)
            result2 = predict_result2(sentences)  # 딥러닝 모델2 호출 및 결과 예측
            print('***model2 OK***')
            print(result2)
            result3 = predict_result3(sentences)  # 딥러닝 모델2 호출 및 결과 예측
            print('***model3 OK***')
            print(result3)
            return JsonResponse({'result': result, 'result2': result2, 'result3': result3})

    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

def about(request):
    return render(request, 'myapp/about.html')