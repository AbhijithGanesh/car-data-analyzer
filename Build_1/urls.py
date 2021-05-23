
from django.contrib import admin
from django.urls import path,include
from Cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage),
    path('Fortuner', FortunerPage),
    path('Harrier', HarrierPage),
    path('Seltos',SeltosPage),
    path('Hector', HectorPage),
    path('XUV500', XUV500Page),
]
