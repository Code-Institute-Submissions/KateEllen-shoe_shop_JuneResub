from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_date_posted = models.DateTimeField(default=timezone.now)
    post_author = models.ForeignKey(User, default="", blank=True,
                                    on_delete=models.CASCADE,
                                    related_name='post')

    class Meta:
        ordering = ['-post_date_posted']

    def __str__(self):
        return self.post_title

class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s -%s' % (self.post, self.name)


