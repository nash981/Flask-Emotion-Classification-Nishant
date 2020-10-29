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

def write_to_csv(idn , result):
    filename='emotion_analysis.txt'
    f=open(filename,'a')
    output = str(idn) + ',' + result + '\n'
    f.write(output)
    f.close()
idn=0;
while(1):
    filename=input("Enter Filename:")
    idn+=1
    if filename == 'exit':
        break
    else:
        url = 'http://127.0.0.1:5000/predict_terminal'
        my_img = {'image': open(filename, 'rb')}
        out = requests.post(url, files=my_img)
        output = out.text
        # convert server response into JSON format.
        print(output)
        write_to_csv(idn,output)
