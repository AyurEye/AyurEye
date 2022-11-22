import os
from django.core.files.storage import FileSystemStorage
from pathlib import Path

from keras.models import load_model
import numpy as np
from django.conf import settings

### DRF components: 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = os.path.join(BASE_DIR, 'models/tb_diagnosis_model.h5')

model = load_model(model_path)


def label_remarks(prediction):
    max_prob_val = np.argsort(prediction)[-1][-1]
    remarks = ' '
    if max_prob_val == 0:
        remarks = "Sorry, you have been infected with Tuberculosis."
    elif max_prob_val == 1:
        remarks = "You are not infected with Tuberculosis, but your lungs is not healthy."
    elif max_prob_val == 2:
        remarks = "You are not infected with tuberculosis, and your lungs is healthy."
    return remarks


def turn_predictions_to_labels(prediction):
    prediction = int(prediction)
    if prediction == 0:
        label = "Tuberculosis"
    elif prediction == 1:
        label = "Sick"
    elif prediction == 2:
        label = "Healthy"
    return label


def calculate_confidence(prediction):
    pre = np.argmax(prediction)
    confidence = prediction[0][pre]
    confidence = int(confidence)
    return confidence


def predict(model, image):
    prediction = model.predict(np.array([image]))
    max_prob_val = np.argmax(prediction)
    label = turn_predictions_to_labels(max_prob_val)
    remarks = label_remarks(prediction)
    confidence = calculate_confidence(prediction)

    if confidence > 100:
        confidence = 100
    if confidence >= 40:
        confidence_remarks = "Confidence: {} %".format(confidence)
    elif confidence < 40:
        confidence_remarks = "Confidence: {}%, Not confident about the image".format(
            confidence)
        label = " "
        remarks = " "

    return label, remarks, confidence_remarks


def upload_image(request):
    f = request.FILES['image']
    fs = FileSystemStorage()
    filePathName = fs.save(f.name, f)
    filePathName = fs.url(filePathName)
    testimage = '.'+filePathName, f

    return testimage, filePathName


def predictImage(testimage, filePathName):
    from keras.preprocessing.image import img_to_array, load_img
    image_width = 512
    image_height = 512

    original = load_img(testimage, target_size=(image_width, image_height))
    numpy_image = img_to_array(original)

    label, remarks, confidence = predict(model, numpy_image)

    return label, remarks, confidence


class Image(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        testimage, filePathName = upload_image(request=request)
        label, remarks, confidence = predictImage(testimage, filePathName)
        response_data = {"label" : label,
                         "remarks" : remarks,
                         "confidence" : confidence,
                        }
        return Response(response_data,
                        status=status.HTTP_202_ACCEPTED)



