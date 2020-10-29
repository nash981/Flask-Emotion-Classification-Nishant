import sys
import os
import glob
import re
from flask import Markup
import json
# Keras
from PIL import Image, ImageOps

# Flask utils
from flask import Flask, redirect, url_for, request, render_template,jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import requests
import csv
import cv2
import math

def write_to_csv(idn , frameno, result):
    filename='emotion_analysis.txt'
    f=open(filename,'a')
    output = str(idn) + ',' + str(frameno) + ',' + result + '\n'
    f.write(output)
    f.close()
idn=0;
videoFile = "test_video.mp4"
imagesFolder = "/home/nash/GitHub/Flask-Emotion-Classification/extracted_imgres"
url = 'http://127.0.0.1:5000/predict_terminal'
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
N = 35*frameRate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(N) == 0):
        idn+=1
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
        my_img = {'image': open(filename, 'rb')}
        out = requests.post(url, files=my_img)
        output=out.text
        print(output)
        write_to_csv(idn,frameId,output)
cap.release()
print ("Done!")
