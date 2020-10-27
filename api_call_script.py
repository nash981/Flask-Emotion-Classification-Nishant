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

def write_to_csv(id , result):
    filename='emotion_analysis.csv'
    f=open(filename,'a')
    f.write(str(id) + ',' + result + '\n')
    f.close()
id=0;
while(1):
    filename=input("Enter Filename:")
    id+=1
    if filename == 'exit':
        break
    else:
        url = 'http://127.0.0.1:5000/predict_terminal'
        my_img = {'image': open(filename, 'rb')}
        out = requests.post(url, files=my_img)
        output = out.text
        # convert server response into JSON format.
        print(output)
        write_to_csv(id,output)


#filepath = '/home/nash/Pictures/WhatsApp Image 2020-10-26 at 02.33.54.jpeg'
