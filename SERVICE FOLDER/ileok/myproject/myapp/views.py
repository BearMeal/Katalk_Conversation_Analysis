
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import predict_models

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file= request.FILES['file']
            result1, result2, result3=predict_models(uploaded_file)
            return JsonResponse({'result': result1, 'result2': result2, 'result3': result3})
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

def about(request):
    return render(request, 'myapp/about.html')