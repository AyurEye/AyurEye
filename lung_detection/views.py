from django.shortcuts import render
from django.conf import settings

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Images
from .serializers import XrayImage



from roboflow import Roboflow


api_key="TBEC47mwgYHscWpwnyue"

rf = Roboflow(api_key=api_key)

project = rf.workspace("kathmandu-university-hqa4p").project("lungabnormalitiesdetection")
model = project.version(1).model

# infer on a local image




class XrayView(APIView):

    def post(self, request, format=None):
        serializer = XrayImage(data=request.data)
        data={}
        if serializer.is_valid():
            image= serializer.save()

            preds = model.predict(image.x_ray.path, confidence=40, overlap=30)
            # media_url = settings.MEDIA_ROOT + settings.MEDIA_URL
            detections = (preds.json()['predictions'])
            x = False if detections ==[] else True
            # addition = {'prediction_parameter':detections, 'disease_detected':x, 'prediction_image':preds.save(f"prediction{image.id}.jpg")}
            image.prediction_parameter=detections
            image.disease_detected=x
            # preds.save(f"{media_url}/prediction{image.id}.jpg")
            # image.prediction_image.path = f"{media_url}/prediction{image.id}.jpg"
            image.save()

            data['response'] = "Successfully submitted image"
            data['xray_path'] = image.x_ray.path
            data['xray_id'] = image.id
            data['disease_detected'] = image.disease_detected
            if image.disease_detected:
                data['prediction_parameter'] = image.prediction_parameter
                # data['prediction_image'] = image.prediction_image.path


            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class XrayDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Images.objects.get(pk=pk)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = XrayImages(image)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)