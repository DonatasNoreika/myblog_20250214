from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=70)
    content = HTMLField(verbose_name="Content", max_length=5000)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Author", on_delete=models.CASCADE)

    def comments_count(self):
        return self.comments.all().count()

    comments_count.short_description = "Comments Count"

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name="Content", max_length=3000)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    author = models.ForeignKey(to=User, verbose_name="Author", on_delete=models.CASCADE)
    post = models.ForeignKey(to="Post", verbose_name="Post", on_delete=models.CASCADE, related_name="comments")


class Photo(models.Model):
    photo = models.ImageField(verbose_name="Nuotrauka", upload_to="post_photos")

    def __str__(self):
        return self.photo.url