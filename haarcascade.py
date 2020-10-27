import cv2
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import os
import sys
IMAGE_SIZE = 128
def extractor(image):
    faceDetector = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
    faces = faceDetector.detectMultiScale(image,1.3,5)
    count = 0
    if faces is not ():
        count = 1
        faces_list = []
        for (x,y,w,h) in faces:
            face = image[y:y+h,x:x+w]
            dim = (IMAGE_SIZE, IMAGE_SIZE)
            resized = cv2.resize(face, dim, interpolation = cv2.INTER_AREA)
            faces_list.append(resized)
    if count == 0:
        return "69"
    else:
        faces_list = np.array(faces_list)
        faces_list = faces_list/225
        n = faces_list.shape
        faces_list = np.reshape(faces_list, (n[0],IMAGE_SIZE,IMAGE_SIZE,1))

        return faces_list