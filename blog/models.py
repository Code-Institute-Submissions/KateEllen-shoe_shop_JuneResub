from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        if not self.title:
            return ""
        else:
            return self.title  # noqa


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s -%s' % (self.post, self.name)


class Characters(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    bio = models.TextField()
    tag_lines = models.TextField()
