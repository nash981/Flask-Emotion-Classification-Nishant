import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf
from predict import*
from haarcascade import*
from flask import Markup

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image, ImageOps

# Flask utils
from flask import Flask, redirect, url_for, request, render_template,jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


image_size = 128
emotions = ['disappointed', 'interested', 'neutral']


print('Model loading...')

def model_predict(img_path):

    image1 = Image.open(img_path)

    open_cv_image = np.array(image1)
    try:
        img_gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    except:
        img_gray = open_cv_image
    faces = extractor(img_gray)
    if faces == "69":
        string = "Enter Proper Picture"
    else:
        pred = predictions(faces)
        string = Markup("The people are {} % {}, {} % {} and {} % {}".format(round(pred[0]*100,2), emotions[0], round(pred[1]*100,2), emotions[1], round(pred[2]*100,2), emotions[2]))

    print('Deleting File at Path: ' + img_path)

    os.remove(img_path)

    print('Deleting File at Path - Success - ')

    return string


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        print('Begin Model Prediction...')

        # Make prediction
        result = model_predict(file_path)

        print('End Model Prediction...')


        return result
    return None
@app.route('/predict_terminal', methods=['GET', 'POST'])
def upload_from_terminal():
    if request.method == 'POST':
        f = request.files['image']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        # Make prediction
        result = model_predict(file_path)


        return jsonify(result)
    return None

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
