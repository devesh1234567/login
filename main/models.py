from django.db import models

# Create your models here.
class  Subscribe(models.Model):
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now=True)

