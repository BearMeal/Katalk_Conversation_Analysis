from django.shortcuts import render

# Create your views here.
def photo_list(req):
    return render(req, 'app1/photo_list.html', {})