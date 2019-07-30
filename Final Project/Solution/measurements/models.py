from django.db import models
from django.db.models import Avg

# Create your models here.

class Area(models.Model):
    """
        Database table named area
        Columns id(int), name (char), longitude and latitude(float)
        Methods with column like behaviours - number_of_location, average_measurement, category_name
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()

    # Returns number of locations in relations with the object
    def number_of_locations(self):
        return Location.objects.filter(area__id=self.id).count()

    # Returns average of all measurements with the object, if empty return None
    def average_measurement(self):
        return Measurement.objects.filter(location__area__id=self.id).aggregate(Avg('value'))['value__avg'] or None

    # Returns a list of category in relations with the object
    def category_name(self):
        return ",".join([x.name for x in Category.objects.filter(members__id=self.id)])

    # Returns column name whenever area object is called
    def __str__(self):
        return self.name

class Location(models.Model):
    """
        Database table named location
        Columns id(int), name (char), altitude (int), area (int) - area id in relations with
    """
    id = models.IntegerField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=50, verbose_name="Name")
    altitude = models.IntegerField(verbose_name="Altitude in feet")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")

    # Returns column name and name of area whenever area object is called
    def __str__(self):
        return "{}:{}".format(self.name, self.area)

class Measurement(models.Model):
    """
        Database table named measurement
        Columns id(int), value(float), date (date format), location (int) location id in relations with
    """
    id = models.IntegerField(primary_key=True, verbose_name="Id")
    value = models.FloatField(verbose_name="Value")
    date = models.DateTimeField(verbose_name="When Taken")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # Returns column name of location whenever area object is called
    def __str__(self):
        return "measurement@{}".format(self.location)

class Category(models.Model):
    """
        Database table named area
        Columns id(int), name (char), description(char), members (int) areas in relations with category
    """
    id = models.IntegerField(primary_key=True, verbose_name="Id")
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.CharField(max_length=100, verbose_name="Description")
    members = models.ManyToManyField(Area, verbose_name="Members")

    # Returns column name whenever area object is called
    def __str__(self):
        return self.name

    class Meta:
        # Table name in plural
        verbose_name_plural = 'Categories'

