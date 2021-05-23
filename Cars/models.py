from django.db import models


class Hector(models.Model):
    Acceleration = models.IntegerField()
    Braking = models.IntegerField()
    gears = models.IntegerField()
    Engine_Temperature = models.IntegerField()
    Battery = models.IntegerField()
    RPM = models.IntegerField()
    Fuel_Burnt = models.IntegerField()
    Distance = models.IntegerField()
    objects = models.Manager()

class Fortuner(models.Model):
    Acceleration = models.IntegerField()
    Braking = models.IntegerField()
    gears = models.IntegerField()
    Engine_Temperature = models.IntegerField()
    Battery = models.IntegerField()
    RPM = models.IntegerField()
    Fuel_Burnt = models.IntegerField()
    Distance = models.IntegerField()
    objects = models.Manager()

class Seltos(models.Model):
    Acceleration = models.IntegerField()
    Braking = models.IntegerField()
    gears = models.IntegerField()
    Engine_Temperature = models.IntegerField()
    Battery = models.IntegerField()
    RPM = models.IntegerField()
    Fuel_Burnt = models.IntegerField()
    Distance = models.IntegerField()
    objects = models.Manager()

class XUV500(models.Model):
    Acceleration = models.IntegerField()
    Braking = models.IntegerField()
    gears = models.IntegerField()
    Engine_Temperature = models.IntegerField()
    Battery = models.IntegerField()
    RPM = models.IntegerField()
    Fuel_Burnt = models.IntegerField()
    Distance = models.IntegerField()
    objects = models.Manager()

class Harrier(models.Model):
    Acceleration = models.IntegerField()
    Braking = models.IntegerField()
    gears = models.IntegerField()
    Engine_Temperature = models.IntegerField()
    Battery = models.IntegerField()
    RPM = models.IntegerField()
    Fuel_Burnt = models.IntegerField()
    Distance = models.IntegerField()
    objects = models.Manager()
    