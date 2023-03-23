from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(req):

    photos=Photo.objects.all()
    return render(req, 'app1/photo_list.html', {'PHOTOS':photos})

def photo_new(req):
    if req.method == 'POST':
        form = PhotoForm(req.POST)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)

    else:
        form = PhotoForm()
        return render(req, 'app1/photo_new.html', {'form':form})
    
def photo_detail(req, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(req, 'app1/photo_detail.html', {'photo':photo})


def photo_edit(req, pk):
    photo=get_object_or_404(Photo, pk=pk)
    if req.method == 'POST':
        form = PhotoForm(req.POST, instance=photo)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)


    form = PhotoForm(instance=photo)
    return render(req, 'app1/photo_new.html', {'form':form})