from django.db import models

# Create your models here.
class Post(models.Model):
    srno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 55)
    author = models.CharField(max_length = 55)
    slug = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return 'Blog from ' + self.author  + self.title