
from django.shortcuts import render
from django.http import JsonResponse
from .forms import UploadFileForm
from .utils import predict_models

async def index(request):
    if request.method == 'POST':
        print('POST ok')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file= request.FILES['file']
            print(uploaded_file)
            result1, result2, result3=await predict_models(uploaded_file)
            print('predict OK')
            return JsonResponse({'result': result1, 'result2': result2, 'result3': result3})
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'myapp/index.html', {'form': form})

def about(request):
    return render(request, 'myapp/about.html')