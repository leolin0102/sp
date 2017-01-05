from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django import forms
from sp import settings
import json
import uuid

class UploadFileForm(forms.Form):
    file = forms.FileField()
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def upload_file_view(request):
    # request.upload_handlers.insert(0, ProgressBarUploadHandler())
    # return _upload_file_view(request)
    form = UploadFileForm(request.POST, request.FILES)
    image_id = None
    if form.is_valid():
        image_id = handle_file_upload(request.FILES['file'])
    return HttpResponse(json.dumps({"status": "200", "imageId": '{}'.format(image_id)}))

def handle_file_upload(f):
    path = settings.SPOT_UPLOAD_IMAGE
    image_id = uuid.uuid1()
    with open('{}/{}.png'.format(path, image_id), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return image_id


