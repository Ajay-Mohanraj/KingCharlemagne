from django.db import models

class Trades(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField()

    def __str__(self):
        return self.id
