from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def upload_file_view(request):
    # request.upload_handlers.insert(0, ProgressBarUploadHandler())
    # return _upload_file_view(request)
    pass
