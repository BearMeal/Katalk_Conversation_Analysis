
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import predict_result2, get_from_txt, save_data_to_db
'''
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = handle_uploaded_file(request.FILES['file'])
            result = predict_result2(txt_file)  # 딥러닝 모델 호출 및 결과 예측
            # os.remove(txt_file)  # 임시 파일 삭제
            prediction_list = result.tolist()
            return JsonResponse({'result': prediction_list})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

'''

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file= request.FILES['file']
            sentences = get_from_txt(uploaded_file)  # 텍스트 파일에서 데이터 추출
            save_data_to_db(sentences)  # 추출된 데이터를 DB에 저장
            result = predict_result2(sentences)  # 딥러닝 모델 호출 및 결과 예측
            # os.remove(txt_file)  # 임시 파일 삭제
            prediction_list = result.tolist()
            return JsonResponse({'result': prediction_list})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

def about(request):
    return render(request, 'myapp/about.html')

def post(request):
    return render(request, 'myapp/post.html')

def detail(request):
    return render(request, 'myapp/detail.html')