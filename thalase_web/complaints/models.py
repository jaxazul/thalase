from django.db import models


class Complaint(models.Model):
    username = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    what_did_you_try = models.CharField(max_length=300)
    date_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'complaint'


