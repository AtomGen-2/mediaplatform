from django.db import models

# Create your models here.
class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)  => this is the auto generated field whenever you create a django model

    content = models.TextField(blank=True, null=True, max_length=240)
    image = models.FileField(upload_to="images/", blank=True, null=True)