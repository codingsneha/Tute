from django.shortcuts import render, redirect
from .forms import TutorialForm
from .models import Tutorial
from .utils import generate_spoken_tutorial

def upload(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tutorial = form.save()
            final_video_path = generate_spoken_tutorial(tutorial.transcript.path, tutorial.video.path)
            tutorial.final_video.name = final_video_path
            tutorial.save()
            return redirect('success')
    else:
        form = TutorialForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    tutorial = Tutorial.objects.latest('id')
    if tutorial.final_video:  # Ensure the file exists
            final_video_url = tutorial.final_video.url
    else:
        final_video_url = None
    return render(request, 'success.html', {'final_video_url': final_video_url})