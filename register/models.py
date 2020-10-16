from django.db import models
from zeal.settings import EMAIL_HOST_USER
from django.core.mail import send_mail



# Create your models here.
class Register(models.Model):

    name    = models.CharField(max_length=50)
    email   = models.EmailField()
    branch  = models.CharField(max_length=25)
    year    = models.CharField(max_length=20)
    document = models.FileField(null = True , blank=True , upload_to = 'documents')   
    
    class Meta:
        db_table = "register"
    

    def __str__(self):
        return self.name
