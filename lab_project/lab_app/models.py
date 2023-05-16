from django.db import models
from datetime import datetime

# Create your models here.


class Reservations(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    reserved_date = models.DateField(auto_now=False, auto_now_add=False)
