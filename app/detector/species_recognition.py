import subprocess
import sys
import re
import os

def recognize(imagePath):
    os.chdir("./detector/yolo/")
    returnValue = subprocess.getoutput("python ./demo.py --imgfile " + imagePath)
    result = returnValue[returnValue.find("seconds.")+9:]
    try:
        result = int(result)
    except ValueError:
        result = 0
    subprocess.getoutput("mv ./predictions.jpg "+imagePath+".recognize.jpeg")
    if result != 0:
        for idx in range(int(result)):
            subprocess.getoutput("mv ./predictions_"+str(idx)+".jpg "+imagePath+"."+str(idx)+".jpeg")
    os.chdir("../../")
    return result