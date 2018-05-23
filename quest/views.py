from django.shortcuts import render

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
def index(request):
	return render(request, 'quest/index.html')