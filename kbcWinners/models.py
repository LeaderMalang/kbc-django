from django.db import models
from django.utils.timezone import now
from django.utils.html import mark_safe

# Create your models here.
class Winner(models.Model):


    #now = timezone.now()
    winner_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField(default=0)
    lottery_number = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField('date published',default=now())

    def image_tag(self):
        return mark_safe('<img src="/images/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Picture'
    image_tag.allow_tags = True

    def __str__(self):
        return self.winner_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email