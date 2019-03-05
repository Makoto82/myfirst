from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.TimeField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title