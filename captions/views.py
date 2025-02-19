from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import Image
from .caption_generator import generate_caption

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            caption = generate_caption(image_instance.image.path)
            image_instance.caption = caption
            image_instance.save()
            return render(request, 'captions/result.html', {'image': image_instance})
    else:
        form = ImageUploadForm()
    return render(request, 'captions/upload.html', {'form': form})

def image_list(request):
    images = Image.objects.all().order_by('-id')
    return render(request, 'captions/list.html', {'images': images})
