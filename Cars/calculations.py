from Cars.models import *
from math import *
def Harrier_processor():
    acc = list(Harrier.objects.values_list('Acceleration', flat = True))
    brk = list(Harrier.objects.values_list('Braking', flat = True))
    grs = list(Harrier.objects.values_list('gears', flat = True))
    rpm = list(Harrier.objects.values_list('RPM', flat = True))
    batt = list(Harrier.objects.values_list('Battery', flat = True))
    dist = list(Harrier.objects.values_list('Distance', flat = True))
    engn_temp = list(Harrier.objects.values_list('Engine_Temperature', flat = True))
    fuel  = list(Harrier.objects.values_list('Fuel_Burnt', flat = True))
    return [acc,brk,grs,rpm,batt,dist,engn_temp,fuel]

def Hector_processor():
    acc = list(Hector.objects.values_list('Acceleration', flat = True))
    brk = list(Hector.objects.values_list('Braking', flat = True))
    grs = list(Hector.objects.values_list('gears', flat = True))
    rpm = list(Hector.objects.values_list('RPM', flat = True))
    batt = list(Hector.objects.values_list('Battery', flat = True))
    dist = list(Hector.objects.values_list('Distance', flat = True))
    engn_temp = list(Hector.objects.values_list('Engine_Temperature', flat = True))
    fuel  = list(Hector.objects.values_list('Fuel_Burnt', flat = True))
    return [acc,brk,grs,rpm,batt,dist,engn_temp,fuel]

def Seltos_processor():
    acc = list(Seltos.objects.values_list('Acceleration', flat = True))
    brk = list(Seltos.objects.values_list('Braking', flat = True))
    grs = list(Seltos.objects.values_list('gears', flat = True))
    rpm = list(Seltos.objects.values_list('RPM', flat = True))
    batt = list(Seltos.objects.values_list('Battery', flat = True))
    dist = list(Seltos.objects.values_list('Distance', flat = True))
    engn_temp = list(Seltos.objects.values_list('Engine_Temperature', flat = True))
    fuel  = list(Seltos.objects.values_list('Fuel_Burnt', flat = True))
    return [acc,brk,grs,rpm,batt,dist,engn_temp,fuel]

def XUV500_processor():
    acc = list(XUV500.objects.values_list('Acceleration', flat = True))
    brk = list(XUV500.objects.values_list('Braking', flat = True))
    grs = list(XUV500.objects.values_list('gears', flat = True))
    rpm = list(XUV500.objects.values_list('RPM', flat = True))
    batt = list(XUV500.objects.values_list('Battery', flat = True))
    dist = list(XUV500.objects.values_list('Distance', flat = True))
    engn_temp = list(XUV500.objects.values_list('Engine_Temperature', flat = True))
    fuel  = list(XUV500.objects.values_list('Fuel_Burnt', flat = True))
    return [acc,brk,grs,rpm,batt,dist,engn_temp,fuel]

def Fortuner_processor():
    acc = list(Fortuner.objects.values_list('Acceleration', flat = True))
    brk = list(Fortuner.objects.values_list('Braking', flat = True))
    grs = list(Fortuner.objects.values_list('gears', flat = True))
    rpm = list(Fortuner.objects.values_list('RPM', flat = True))
    batt = list(Fortuner.objects.values_list('Battery', flat = True))
    dist = list(Fortuner.objects.values_list('Distance', flat = True))
    engn_temp = list(Fortuner.objects.values_list('Engine_Temperature', flat = True))
    fuel  = list(Fortuner.objects.values_list('Fuel_Burnt', flat = True))
    return [acc,brk,grs,rpm,batt,dist,engn_temp,fuel]



def avg(lst):
    return sum(lst)/len(lst)  

def mileage(lst1, lst2):
    return avg(lst1)/avg(lst2)

def Car_Score(lst):
    score = 0
    for i in lst:
        value = i[0]*i[2]-i[1]+i[3]
        score += value
    return score/len(max(lst))

def rpm_gear(lst):
        ideal_list = [(7786+4687)/2, (4980+7069)/2 , (5108+6794)/2 , (5255+6456)/2, 6456]
        valdict = {}
        additionallst = [[], [], [], [] , []]
        grs = lst[2]
        rpm = lst[3]
        for i in range(len(rpm)):
            if grs[i] == 1:
                additionallst[0].append(rpm[i])
            elif grs[i] == 2:
                additionallst[1].append(rpm[i])
            elif grs[i] == 3:
                additionallst[2].append(rpm[i])
            elif grs[i] == 4:
                additionallst[3].append(rpm[i]) 
            elif grs[i] == 5:
                additionallst[4].append(rpm[i])
        for i in range(len(additionallst)):
            valdict[ideal_list[i]] = round(avg(additionallst[i]),2)
        return valdict

def brakestress(lst):
    return round(avg(lst[1]),2)

def tempgrad(lst):
    dst = lst[-3]
    temp = lst[-2]
    deltad = []
    deltat = []
    for i in range(1,len(temp)):
        try:
            deltat.append(temp[i]-temp[i-1])
            deltad.append(dst[i]-dst[i-1])
        except TypeError:
            deltat.append(0)
            deltad.append(0)
    return round(avg(deltat)/avg(deltad)*1000,2)
