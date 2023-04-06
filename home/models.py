from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(default='',max_length=123)
    lname=models.CharField(default='',max_length=123)
    email=models.EmailField()
    phone=models.CharField(default='',max_length=12)
    text=models.TextField()

    def __str__(self) -> str:
        return self.fname


