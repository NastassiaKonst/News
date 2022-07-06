from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    header = models.CharField(max_length=100)
    annotation = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


    def __str__(self):
        return self.header


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.surname


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    comment_date = models.DateTimeField()
    comment = models.TextField()


