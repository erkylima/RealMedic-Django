from django.db import models

class LatLng(models.Model):
    class Meta:
        verbose_name = 'LatLng'
        verbose_name_plural = 'LatLngs'

    lat = models.FloatField()
    lng = models.FloatField()
    def __str__(self):
        return '{0} - {1}'.format(str(self.lat), str(self.lng))
