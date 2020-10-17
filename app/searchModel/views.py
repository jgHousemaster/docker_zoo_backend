from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json
from searchImage.models import Query
from searchModel.models import QueryThree

# Create your views here.


def requestModel(request):
    if request.method == "POST":
        reqData = json.loads(request.body.decode())
        retData = {}
        dt = Query.objects.filter(id=reqData["id"])
        if len(dt) > 0 and reqData["subId"] <= dt[0].result:
            retData["status"] = dt[0].status
            if dt[0].status == "done":
                QueryThree.objects.create(
                    id=reqData["id"],
                    subId=reqData["subId"],
                    status="pending",
                    requestTime=timezone.now(),
                )
        else:
            retData["status"] = "not found"
        return HttpResponse(json.dumps(retData))
    else:
        return HttpResponse("status: test_ok")
