import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import predict_result
from .models import UploadedFile

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = handle_uploaded_file(request.FILES['file'])
            result = predict_result(txt_file)  # 딥러닝 모델 호출 및 결과 예측
            # os.remove(txt_file)  # 임시 파일 삭제
            prediction_list = result.tolist()
            print(len(prediction_list), len(prediction_list[0]))
            return JsonResponse({'result': prediction_list})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

def handle_uploaded_file(file):
    uploaded_file = UploadedFile(file=file)
    uploaded_file.file.save(file.name, file, save=True)
    uploaded_file.save()
    return uploaded_file.file.path

def about(request):
    return render(request, 'myapp/about.html')

def post(request):
    return render(request, 'myapp/post.html')

def contact(request):
    return render(request, 'myapp/contact.html')