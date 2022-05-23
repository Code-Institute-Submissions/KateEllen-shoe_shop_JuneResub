from django.db import models


class Signup(models.Model):
    """
    Model for signing up for the mailing list
    """

    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
