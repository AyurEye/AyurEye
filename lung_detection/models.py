from django.db import models

# Create your models here.
class Images(models.Model):
    id = models.AutoField(primary_key=True)
    x_ray = models.ImageField(upload_to='media/', blank=True, null=True)
    disease_detected = models.BooleanField(blank=True, null=True)
    prediction_image = models.TextField(blank=True, null=True)
    prediction_parameter = models.TextField(blank=True, null=True)

    

