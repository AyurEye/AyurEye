from django.conf.urls import url
from django.urls import path
from prediction_api.views import Image


urlpatterns = [
    url(r'^image/$', Image.as_view(), name='upload-image'),
]