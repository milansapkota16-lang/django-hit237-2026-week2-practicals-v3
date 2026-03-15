from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    published_date = models.DateTimeField()


    def __str__(self):
        return self.title[:25]
# Create your models here.
