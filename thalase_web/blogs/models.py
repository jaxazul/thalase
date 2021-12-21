from django.db import models


# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    content = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blog'
