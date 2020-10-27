from tensorflow.keras.models import load_model
import numpy as np

def predictions(images):
    model = load_model('models/facial_expression_densenet201v2.h5')
    pred = model.predict(images)
    pred = np.mean(pred,axis = 0)
    return pred