from django.db import models

# Create your models here.

class Profile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_name