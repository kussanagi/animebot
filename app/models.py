from django.db import models

class Title(models.Model):
    name = models.CharField(max_length=200)
    episodes = models.CharField(max_length=4, default='', blank=True, null=True)
    release_date = models.CharField(max_length=50, default='', blank=True, null=True)

    def __str__(self):
        return self.name