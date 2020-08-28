from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120,null=True)
    description = models.CharField(max_length=120)
    body = models.CharField(max_length=120)

    def __str__(self):
        return self.author