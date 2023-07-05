from django.db import models

# Create your models here.


class Wish(models.Model):
    name_of_person_being_wished = models.CharField(max_length=1000)
    mail_of_person_being_wished = models.EmailField(null=True, blank=True)
    name_of_person_doing_wishing = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    wish_message = models.TextField()
    date_and_time = models.DateTimeField()



class WishMedia(models.Model):
    image = models.ImageField(upload_to='media')
    video = models.FileField(upload_to='media')
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE)