from django.shortcuts import render, get_object_or_404, redirect
from .models import App1
from .forms import PhotoForm


# Create your views here.
def photo_list(req):
    photos=App1.objects.all()

    return render(req, 'app1/photo_list.html', {'photos':photos})

def photo_detail(req,pk):
    photo = get_object_or_404(App1,pk=pk)
    return render(req, 'app1/photo_detail.html', {'photo':photo})

def photo_post(req):
    if req.method == "POST":
        form = PhotoForm(req.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form=PhotoForm()
    return render(req, 'app1/photo_post.html', {'form':form})
        
def photo_edit(req, pk):
    photo = get_object_or_404(App1, pk=pk)
    if req.method=="POST":
        form=PhotoForm(req.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form=PhotoForm(instance=photo)
    return render(req, 'app1/photo_post.html', {'form':form})