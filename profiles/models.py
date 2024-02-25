from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    Creates a profile so that the user can save their default 
    delivery address and view their order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
