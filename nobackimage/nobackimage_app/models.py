from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="documents/", default="defo", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.image.url
    