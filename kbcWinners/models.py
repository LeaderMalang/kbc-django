from django.db import models

# Create your models here.
class Winner(models.Model):
    winner_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField(default=0)
    lottery_number = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email