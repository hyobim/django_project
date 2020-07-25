from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    SHIRT_SIZES = (
      ('S', '선명하게'),
      ('M', '뽀얗게'),
      ('L', '분위기있게'),
      ('L', '시크하게'),
  )

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    style = models.CharField(max_length=1,choices=SHIRT_SIZES)
    image = models.ImageField(upload_to='images/',blank=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)