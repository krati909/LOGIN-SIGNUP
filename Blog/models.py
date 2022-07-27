from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    image=models.FileField(null=True, blank=True,upload_to="images")
    category=models.CharField(max_length=100,null=True, blank=True,choices=(( 'Mental Health','Mental Health'),('Heart Disease','Heart Disease') ,('Covid19','Covid19'),('Immunization','Immunization')))
    summary = models.TextField(max_length=100,null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)
    draft=models.BooleanField(default=False)
    user=models.CharField(max_length=100,null=True, blank=True)