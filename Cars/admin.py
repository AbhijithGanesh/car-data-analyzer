from django.contrib import admin

from .models import *

myModels = [Harrier,Hector,Fortuner,Seltos,XUV500]
admin.site.register(myModels)
