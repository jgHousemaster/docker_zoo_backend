from django.shortcuts import render
from django.http import HttpResponse
from animalInfo.models import AnimalInfo
import json

# Create your views here.


def index(request, id):
    if request.method == "POST":
        retData = {}
        dt = AnimalInfo.objects.filter(id=id)
        if len(dt) > 0:
            retData["status"] = "ok"
            retData["name"] = dt[0].name
        else:
            retData["status"] = "not found"
        return HttpResponse(json.dumps(retData))
    return HttpResponse("status: ok")
