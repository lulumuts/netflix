from django.db import models

# Create your models here.
class Carousel(models.Model):

    image=models.ImageField(upload_to = 'img/',blank=True)
    image_name= models.CharField(max_length=100)

    def __str__(self):
        return self.image_name

    @classmethod
    def show_all(cls):
        images = cls.objects.all()
        return images

class Movie:

    def __init__(self,id,title,poster_path,overview,vote_average):

        self.id=id
        self.title=title
        self.poster_path="https://image.tmdb.org/t/p/w500/" + poster_path
        self.overview=overview
        self.vote_average=vote_average
