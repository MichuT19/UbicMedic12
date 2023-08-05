import openpyxl
from django.db import models
from django.contrib.gis import admin
# Create your models here.

# from home.administrador.models import *
# from home.enfermero.models import *
# from home.paciente.models import *

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from home.reportes.reportes_excel.admin import *
#from home.reportes.reportes_pdf.admin import *

class Marker1(models.Model):
    id = models.AutoField(primary_key=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6) 
    ubicacion = models.PointField()

    def save(self,*args,**kwagrs):
        if not self.latitud:
            self.latitud=self.ubicacion.y
        if not self.longitud:
            self.longitud=self.ubicacion.x
        super(Marker1,self).save(*args,**kwagrs)

# @admin.register(Marker1)
# class MarkerAdmin(admin.OSMGeoAdmin):
#     list_display = ('id','latitud','longitud','ubicacion')
#     readonly_fields=('longitud','latitud')
#     #actions=[reportmarket_pais]
    

#  marker1= Marker1.objects.get(pk=1)
#  latitud = marker1.location.y
#  lonitud = marker1.location.x





    

  



  




