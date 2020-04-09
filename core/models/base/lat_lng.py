from django.db import models

from core.models.base.time_stampable import Timestampable
from core.util.util_manager import UpperCaseCharField


class LatLng(models.Model):
    class Meta:
        verbose_name = 'LatLng'
        verbose_name_plural = 'LatLngs'

    lat = models.DecimalField(max_digits='100', decimal_places=0, max_length=100)
    lng = models.DecimalField(max_digits='100', decimal_places=0, max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.lat, self.lng)
