
from django.contrib import admin
from .models import PCR,RoadCityCenter,CityCenterNode,LatLon,Geomet,survey1,survey2,survey3,survey4,serviceproviderlocation,shapefile,shapefilepoint


# Register your models here.
admin.site.register(Geomet)
admin.site.register(PCR)
admin.site.register(RoadCityCenter)
admin.site.register(CityCenterNode)
admin.site.register(LatLon)
admin.site.register(survey4)
admin.site.register(survey1)
admin.site.register(survey2)
admin.site.register(survey3)
admin.site.register(serviceproviderlocation)
admin.site.register(shapefile)
admin.site.register(shapefilepoint)

