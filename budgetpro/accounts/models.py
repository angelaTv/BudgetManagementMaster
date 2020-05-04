from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=120)
    Address = models.TextField(max_length=120)
    email = models.EmailField()
    username = models.CharField(max_length=120)
    mobile_no = models.IntegerField()
    password = models.CharField(max_length=120)
    is_Active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
