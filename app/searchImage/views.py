from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from searchImage.models import Query
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.conf import settings
from PIL import Image
import json
#import datetime
from django.utils import timezone
import uuid
import os

# Create your views here.

def upload(request):
    if request.method == "POST":
        retData = {}
        img_f = request.FILES.get('pic', None)
        if img_f == None:
            retData["status"] = "error"
            retData["discription"] = "No Image has been uploaded"
            return HttpResponse(json.dumps(retData))
        id = str(uuid.uuid4())
        pic_io = BytesIO()
        img = Image.open(img_f)
        img = img.convert("RGB")
        img.save(pic_io, "jpeg")
        pic_file = InMemoryUploadedFile(
            file = pic_io,
            field_name = None,
            name = id + ".jpeg",
            content_type = "image_jpeg",
            size = img_f.size,
            charset = None
        )
        Query.objects.create(id = id, 
                            img = pic_file, 
                            status = "pending", 
                            submitTime = timezone.now())
        retData["status"] = "ok"
        retData["id"] = id
        return HttpResponse(json.dumps(retData))
    return HttpResponse("status: test_ok")

def getStatus(request):
    if request.method == "POST":
        reqData = json.loads(request.body.decode())
        retData = {}
        dt = Query.objects.filter(id = reqData["id"])
        if len(dt) > 0:
            retData["status"] = dt[0].status
            if dt[0].status == "done":
                retData["result"] = dt[0].result
                retData["individualRes"] = dt[0].individualRes
        else:
            retData["status"] = "not found"
        return HttpResponse(json.dumps(retData))
    return HttpResponse("status: test_ok")

def getPic(request, id):
    retData = {}
    dt = Query.objects.filter(id = id)
    if len(dt) > 0:
        fn = settings.BASE_DIR + dt[0].img.url + ".recognize.jpeg"
        file = open(fn, "rb")
        response = FileResponse(file)
        response["Content-Type"] = "application/jpeg-stream"
        response["Content-Disposition"] = 'attachment;filename="1.jpeg"'
        return response
    else:
        retData["status"] = "not found"
        return HttpResponse(json.dumps(retData))
