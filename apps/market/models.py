from django.db import models
from django.contrib.gis.db import models as gismodels


class Market(models.Model):
    store = models.CharField(
        max_length=100, verbose_name='Nombre de la tienda', unique=True)
    geos = gismodels.PointField(verbose_name='Ubicación')

    def __str__(self):
        return self.store
