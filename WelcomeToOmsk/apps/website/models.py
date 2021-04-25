from django.db import models


class Sight(models.Model):
    sight_name = models.CharField(max_length=200)
    sight_photo = models.ImageField(max_length=500)
    sight_description = models.CharField(max_length=500)
    sight_address = models.CharField(max_length=200)
    sight_history = models.TextField()
    sight_link = models.CharField(max_length=700)

    def __str__(self):
        return self.sight_name

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'
