from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True,max_length=255)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'
    def get_username(self):
        return self.email

class Events(models.Model):
    owner = models.ForeignKey(User ,related_name='events' ,on_delete=models.CASCADE )
    title = models.CharField(max_length=255,unique=True)
    startDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    iscompleted = models.BooleanField(null=False)
    REQUIRED_FIELDS = ['owner','startDateTime','endDateTime','isCompleted','title']
    def clean(self):
        super().clean()
        if not (timezone.now() <= self.startDateTime <= self.endDateTime):
            raise ValidationError('Invalid start and end datetime')
    def get_title(self):
        return self.title





# Create your models here.
