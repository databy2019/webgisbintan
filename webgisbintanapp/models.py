from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager

# Create your models here.
class bataskabupaten(models.Model):
    #definisi model/table
    kode = models.CharField(max_length=30)
    kabupaten = models.CharField(max_length=30)
    geometry = gis_models.PolygonField(srid=4326)
    objects = GeoManager()

    def __self__ (self):
        return self.title

    class Meta():
        verbose_name_plural = 'Batas Kabupaten'

