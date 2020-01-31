from . import views
from django.conf.urls import url


urlpatterns =[
url(r'point$', views.newlatlonview, name='newlatlonview'),
url(r'form$', views.form, name='form'),]