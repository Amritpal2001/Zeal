from django.db import models

# Create your models here.
status = (
   ('member', 'member'),
   ('developer', 'developer'),
   ('core','core'),
   ('fac' ,'fac'),
)

class Team(models.Model):

    name            = models.CharField(max_length=45)
    designation     = models.CharField(max_length=45)
    images          = models.ImageField(upload_to= 'images/team',default='' , blank=True , null=True  )
    linkedin        = models.URLField()
    status          = models.CharField(choices=status, max_length=128)
    role            = models.TextField()

    def __str__(self):
        return self.name

    
