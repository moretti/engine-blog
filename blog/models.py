from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

