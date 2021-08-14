from django.db import models

class BlogPost(models.Model):
    """A BlogPost the user is posting on Blog."""
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return a string representaation of the model."""
        return self.title

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