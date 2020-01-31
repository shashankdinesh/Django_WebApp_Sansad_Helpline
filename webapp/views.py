from django.shortcuts import render
from rest_framework import viewsets,status
from .models import PCR,RoadCityCenter,CityCenterNode,LatLon,Geomet, \
    serviceproviderlocation,survey1,survey2,survey3,survey4,shapefilepoint,shapefile
from math import radians, cos, sin, asin, sqrt, atan2, degrees
import json
from . import load
from webapp.shorts.teststage5 import main

# Create your views here.


def form(request):

    return render(request,'Home.html', {'title':'YOUR LOCATION'})

def loaders(request):
    l1,l2=[],[]
    dictionary={}
    t = shapefile.object.all()
    for h in range(len(t)):
        geojson = t[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        l1.append(coordinates)
    q = shapefilepoint.object.all()
    for h in range(len(q)):
        geojson = q[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        l2.append(coordinates)
    dictionary['coord1']=l1
    dictionary['coord']=l2
    return render(request, "loader.html",dictionary)


def newlatlonview(request):
    poli={}
    holi=[]
    l1 = []
    coord=[]
    plat,plon=None,None
    a=LatLon.object.all()
    for w in a:
        coord.append([w.lat,w.lon])

    clat = a[len(a) - 1].lat
    clon = a[len(a) - 1].lon
    pointA=(clon,clat)
    kj = serviceproviderlocation.object.all()
    if len(kj) is not 0:
        for i in range(len(kj)):
            plat = kj[i].lat
            plon = kj[i].lon
            pointB = (plon, plat)
            poli[haversine(pointA, pointB)] = pointB
            holi.append(haversine(pointA, pointB))
        s = poli[min(holi)]
        main(s[0], s[1], pointA[0], pointA[1],"C:/Users\Hp\Desktop\DATA","SHORTROUTE",fruit=[])
        Geomet.object.all().delete()
        load.FUR()
        t = Geomet.object.all()
        for h in range(len(t)):
            geojson = s[h].mpoly.json
            coordinates = json.loads(geojson).get('coordinates')
            l1.append(coordinates)
    else:
        b = PCR.object.all()
        for i in range(len(b)):
            plat = b[i].lat
            plon = b[i].lon
            pointB = (plon, plat)
            poli[haversine(pointA, pointB)] = pointB
            holi.append(haversine(pointA, pointB))
        s = poli[min(holi)]
        plon=s[0]
        plat=s[1]
        print(s[0], s[1],"policeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        main(s[0], s[1], pointA[0], pointA[1],"C:/Users\Hp\Desktop\DATA","SHORTROUTE",fruit=[])
        Geomet.object.all().delete()
        load.FUR()
        t = Geomet.object.all()
        for h in range(len(t)):
            geojson = t[h].mpoly.json
            coordinates = json.loads(geojson).get('coordinates')
            l1.append(coordinates)

    s1=survey1.object.all()
    s1lat = s1[len(s1) - 1].lat
    s1lon = s1[len(s1) - 1].lon
    '''main(s1lon, s1lat, pointA[0], pointA[1],"C:/Users\Hp\Desktop\DATA","SURVEY1",fruit=[])
    survey1karasta.object.all().delete()
    load.survey1ras()
    su1 = survey1karasta.object.all()
    sul1 = []
    for h in range(len(su1)):
        geojson = su1[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        sul1.append(coordinates)'''

    s2 = survey2.object.all()
    s2lat = s2[len(s2) - 1].lat
    s2lon = s2[len(s2) - 1].lon
    '''main(s2lon, s2lat, pointA[0], pointA[1], "C:/Users\Hp\Desktop\DATA", "SURVEY2",fruit=[])
    survey2karasta.object.all().delete()
    load.survey2ras()
    su2 = survey2karasta.object.all()
    sul2 = []
    for h in range(len(su2)):
        geojson = su2[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        sul2.append(coordinates)'''

    s3 = survey3.object.all()
    s3lat = s3[len(s3) - 1].lat
    s3lon = s3[len(s3) - 1].lon
    '''main(s3lon, s3lat, pointA[0], pointA[1], "C:/Users\Hp\Desktop\DATA", "SURVEY3",fruit=[])
    survey3karasta.object.all().delete()
    load.survey3ras()
    su3 = survey3karasta.object.all()
    sul3 = []
    for h in range(len(su3)):
        geojson = su3[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        sul3.append(coordinates)'''

    s4 = survey4.object.all()
    s4lat = s4[len(s4) - 1].lat
    s4lon = s4[len(s4) - 1].lon
    '''main(s4lon, s4lat, pointA[0], pointA[1], "C:/Users\Hp\Desktop\DATA", "SURVEY4",fruit=[])
    survey4karasta.object.all().delete()
    load.survey4ras()
    su4 = survey4karasta.object.all()
    sul4 = []
    for h in range(len(su4)):
        geojson = su4[h].mpoly.json
        coordinates = json.loads(geojson).get('coordinates')
        sul4.append(coordinates)'''
    londe=[[ s1lat,s1lon],[ s2lat,s2lon],[ s3lat,s3lon],[ s4lat,s4lon]]
    latitude=[s1lat, s2lat,s3lat,s4lat]
    longitude=[s1lon,s2lon,s3lon,s4lon]
    latitude.append(float(plat))
    longitude.append(float(plon))
    latitude.append(float(clat))
    longitude.append(float(clon))
    n = max(latitude)
    s = min(latitude)
    e = max(longitude)
    w = min(longitude)
    dictionary = {'title': 'closest_service', 'pm': plat, 'pn': plon, 'cm': clat, 'cn': clon, 'coord1': l1,
                 'londe':londe,'coord':coord,'north':n,'south':s,'east':e,'west':w}

    return render(request, 'example.html', dictionary)

def haversine(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = pointA[1]
    lon1 = pointA[0]

    lat2 = pointB[1]
    lon2 = pointB[0]

    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r
