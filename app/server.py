# django setup
import os, sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MobileZoo.settings")
django.setup()
from django.conf import settings

# django setup done
import time
import detector.species_recognition as species_recognition
import detector.red_panda.test as redpanda_recognition
import os
from searchImage.models import Query
from django.utils import timezone

while True:
    objs = Query.objects.filter(status="pending")
    if len(objs) > 0:
        obj = objs[0]
        # print("Found: " + str(obj.id))
        obj.status = "recognizeing"
        obj.save()
        fn = settings.BASE_DIR + obj.img.url
        # print(fn)
        Res = ""
        individualRes = ""
        try:
            Res = species_recognition.recognize(fn)
            # Res = "red panda"
            print(Res)
            if Res.find("red panda") != -1:
                individualRes += redpanda_recognition.recognize(fn)
        except:
            obj.status = "error"
        obj.result = Res
        obj.individualRes = individualRes
        obj.recognizeTime = timezone.now()
        obj.status = "done"
        obj.save()
    time.sleep(0.5)
