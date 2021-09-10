from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """A BlogPost the user is posting on Blog."""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """Return a string representaation of the model."""
        return self.text

class Entry(models.Model):
    """Post"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."