from django.contrib import admin
from django.urls import path
from cv.views import *

app_name = 'cv'

urlpatterns = [
    path('',index_view,name= 'index'),
    path('languages',about_view,name='languages'),
    path('education',education_view,name='education'),
    path('abilities',Abilities_view,name='abilities'),
    path('contact',contact_view,name= 'contact')

    
]