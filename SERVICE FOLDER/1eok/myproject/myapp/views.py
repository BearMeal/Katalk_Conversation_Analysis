import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import handle_uploaded_file, predict_result

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = handle_uploaded_file(request.FILES['file'])
            result = predict_result(txt_file)  # 딥러닝 모델 호출 및 결과 예측
            os.remove(txt_file)  # 임시 파일 삭제
            return JsonResponse({'result': result})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})