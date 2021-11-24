from datetime import datetime
from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        time = datetime.now()
        super(Enquiry, self).save()

