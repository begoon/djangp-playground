from django.db import models

# Create your models here.


class Main(models.Model):
    settings = models.JSONField()
