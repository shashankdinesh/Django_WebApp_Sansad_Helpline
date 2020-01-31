from django.contrib.gis.utils import LayerMapping
from .models import RoadCityCenter,CityCenterNode,Geomet,shapefile,shapefilepoint


dics={'mpoly': 'POINT','name':'name'}
var="C:/Users\Hp\Desktop\DATA\SANSADNODES\SANSADNODES.shp"
def run (verbose=True):
    CityCenterNode.object.all().delete()
    lm =LayerMapping(CityCenterNode,var,dics,transform=False,encoding='iso-8859-1',)
    lm.save(strict=True,verbose=verbose)

dics_2={'mpoly': 'LINESTRING','name':'name'}
var_2="C:/Users\Hp\Desktop\DATA\SANSADLINES\SANSADLINES.shp"
def NUR (verbose=True):
    RoadCityCenter.object.all().delete()
    lm =LayerMapping(RoadCityCenter,var_2,dics_2,transform=False,encoding='iso-8859-1',)
    lm.save(strict=True,verbose=verbose)

dics_3={'mpoly': 'LINESTRING'}
var_3="C:/Users\Hp\Desktop\DATA\SHORTROUTE\SHORTROUTE.shp"
def FUR (verbose=True):
    lm =LayerMapping(Geomet,var_3,dics_3,transform=False,encoding='iso-8859-1',)
    lm.save(strict=True,verbose=verbose)

dics_22={'mpoly': 'POINT'}
var_22="C:/Users\Hp\Desktop\DATA\COMBINEPOINT\COMBINEPOINT.shp"
def shapepoint (verbose=True):
    shapefilepoint.object.all().delete()
    lm =LayerMapping(shapefilepoint,var_22,dics_22,transform=False,encoding='iso-8859-1',)
    lm.save(strict=True,verbose=verbose)

dics_23={'mpoly': 'LINESTRING'}
var_23="C:/Users\Hp\Desktop\DATA\COMBINE\COMBINE.shp"
def shape (verbose=True):
    shapefile.object.all().delete()
    lm =LayerMapping(shapefile,var_23,dics_23,transform=False,encoding='iso-8859-1',)
    lm.save(strict=True,verbose=verbose)