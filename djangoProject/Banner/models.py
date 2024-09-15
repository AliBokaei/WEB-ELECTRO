from django.db import models


# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=200)  # h1
    description = models.TextField()  # paragraph
    image = models.ImageField(upload_to='banners/')
    link = models.URLField()

    def __str__(self):
        return self.title
