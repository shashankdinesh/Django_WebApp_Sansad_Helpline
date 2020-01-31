from django.db import models
from django.contrib.gis.db import models
import datetime

# Create your models here.

class CityCenterNode(models.Model):
    mpoly = models.PointField()
    name = models.CharField(max_length=500, null=True)
    object = models.Manager()

class RoadCityCenter(models.Model):
    mpoly = models.LineStringField()
    name=models.CharField(max_length=500, null=True)
    object = models.Manager()
class PCR(models.Model):
    pcrid = models.CharField(max_length=50, null=True)
    num_of_members = models.PositiveIntegerField(null=True)
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()

class LatLon (models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()

class Geomet (models.Model):
    mpoly = models.LineStringField(null=True)
    object = models.Manager()

class survey1(models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()


class survey2 (models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()
class survey3 (models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()
class survey4 (models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()

class serviceproviderlocation (models.Model):
    lat = models.FloatField(max_length=50, null=True)
    lon = models.FloatField(max_length=50, null=True)
    object = models.Manager()

class shapefile (models.Model):
    mpoly = models.LineStringField(null=True)
    object = models.Manager()

class shapefilepoint (models.Model):
    mpoly = models.PointField(null=True)
    object = models.Manager()