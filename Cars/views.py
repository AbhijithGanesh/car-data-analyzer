from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,View
from Cars.models import *
from math import *
from Cars.calculations import *

def landingpage(request):   
    return render(request, "Cars/Landing_Page.html")
  
def SeltosPage(request):
    data = "Seltos"
    Image = f"/static/Cars/images/{data}.jpg"
    ds = Seltos_processor()
    milg = round(mileage(ds[5],ds[-1] ),2)
    score = round(Car_Score(ds),2)
    grdnt = tempgrad(ds)
    rpmdata = rpm_gear(ds)
    return render(request, 'Cars/Seltos.html', {"data":data, "image":Image,"Car_Name":data,
                                                  "Gradient":grdnt,
                                                  "Brake_Stress":brakestress(ds),
                                                  "Car_Mileage": milg, 
                                                  "Car_Score":round(score, 2),
                                                  "rpmdata":rpmdata})


def HarrierPage(request):
    data = "Harrier"
    Image = "/static/Cars/images/Harrier.jpg"
    ds = Harrier_processor()
    milg = round(mileage(ds[5],ds[-1] ),2)
    score = round(Car_Score(ds),2)
    rpmdata = rpm_gear(ds)
    grdnt = tempgrad(ds)
    return render(request, 'Cars/Harrier.html', {"data":data, "image":Image,"Car_Name":data,
                                                  "Gradient":grdnt,
                                                  "Brake_Stress":brakestress(ds),
                                                  "Car_Mileage": milg, 
                                                  "Car_Score":round(score, 2),
                                                  "rpmdata":rpmdata})

def XUV500Page(request):
    data = "XUV500"
    Image = f"/static/Cars/images/{data}.jpg"
    ds = XUV500_processor()
    milg = round(mileage(ds[5],ds[-1] ),2)
    grdnt = tempgrad(ds)
    score = round(Car_Score(ds),2)
    rpmdata = rpm_gear(ds)
    return render(request, 'Cars/XUV500.html', {"data":data, "image":Image,"Car_Name":data,
                                                  "Gradient":grdnt,
                                                  "Brake_Stress":brakestress(ds),
                                                  "Car_Mileage": milg, 
                                                  "Car_Score":round(score, 2),
                                                  "rpmdata":rpmdata})
    
def HectorPage(request):
    data = "Hector"
    Image = f"/static/Cars/images/{data}.jpg"
    ds = Hector_processor()
    milg = round(mileage(ds[5],ds[-1] ),2)
    score = round(Car_Score(ds),2)
    grdnt = tempgrad(ds)
    rpmdata = rpm_gear(ds)
    brkstrs = brakestress(ds)
    return render(request, 'Cars/Hector.html',{"data":data, "image":Image,"Car_Name":data,
                                                  "Gradient":grdnt,
                                                  "Brake_Stress":brakestress(ds),
                                                  "Car_Mileage": milg, 
                                                  "Car_Score":round(score, 2),
                                                  "rpmdata":rpmdata})

def FortunerPage(request):
    data = "Fortuner"
    Image = f"/static/Cars/images/{data}.jpg"
    ds = Fortuner_processor()
    grdnt = tempgrad(ds)
    milg = round(mileage(ds[5],ds[-1] ),2)
    score = round(Car_Score(ds),2)
    rpmdata = rpm_gear(ds)
    return render(request, 'Cars/Fortuner.html', {"data":data, "image":Image,"Car_Name":data,
                                                  "Gradient":grdnt,
                                                  "Brake_Stress":brakestress(ds),
                                                  "Car_Mileage": milg, 
                                                  "Car_Score":round(score, 2),
                                                  "rpmdata":rpmdata})
