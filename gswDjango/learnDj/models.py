from django.db import models
from django.utils import timezone
# Create your models here.

class LearnDjnago (models.Model):
    LEARN_DJANGO = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default= timezone.now)
    type = models.CharField(max_length=2, choices = LEARN_DJANGO)

