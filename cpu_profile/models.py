from django.db import models

class Records(models.Model):
    date_time = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.date_time, self.value)