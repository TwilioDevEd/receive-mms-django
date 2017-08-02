from django.db import models


class MMSMedia(models.Model):
    filename = models.CharField(max_length=30)
    mime_type = models.CharField(max_length=30) 
    media_sid = models.CharField(max_length=35)
    message_sid = models.CharField(max_length=35)
    media_url = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.filename
