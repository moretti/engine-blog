from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
