from django.db import models
import uuid
class Rooms(models.Model):
    id = models.CharField(max_length=50, blank=True, primary_key=True)