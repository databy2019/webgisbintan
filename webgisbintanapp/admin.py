from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
#from leaflet.admin import LeafletGeoAdmin
from .models import bataskabupaten

# Register your models here.
class BataskabupatenAdmin(OSMGeoAdmin):
    list_display = ('kode', 'kabupaten')
    search_fields = ('kabupaten',)
    filter_fields = ('kode','kabupaten')

    default_lat = 114350.81050
    default_lon = 11637527.43482
    default_zoom = 10
 

admin.site.register(bataskabupaten, BataskabupatenAdmin)
