from django.db import models

# Create your models here.
class watchlist(models.Model) :
    title = models.CharField(max_length=256, unique=True, blank=True)
