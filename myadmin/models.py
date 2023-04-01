from django.db import models

# Create your models here.


class Tour(models.Model):
    tour_quote = models.CharField(max_length=200)
    tour_description = models.TextField()
    tour_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.tour_quote


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_description = models.TextField()
    location_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.location_name
class About(models.Model):
    about_image = models.ImageField(upload_to='images/')


class Package(models.Model):
    package_name = models.CharField(max_length=200)
    package_description = models.TextField()
    package_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.package_name
class TravelOffer(models.Model):
    discount= models.CharField(max_length=200)
    title= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class RecentPost(models.Model):
    title= models.CharField(max_length=100)
    post_by= models.CharField(max_length=100)
    date=models.DateField()
    comment= models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class TourGuide(models.Model):
    place= models.CharField(max_length=100)
    agent= models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    facebook= models.URLField(max_length=200)
    twitter= models.URLField(max_length=200)
    instagram= models.URLField(max_length=200)
    linkedin= models.URLField(max_length=200)
    def __str__(self):
        return self.place

class Contact(models.Model):
    TOUR_CHOICES = (
        ("SOLO_TRAVELLER","Solo Traveller"),
        ("GROUP_OF_PEOPLE","Group of People"),
        ("GROUP_OF_ORGANSATION","Group of Organisation"),
        ("OTHERS","Others"),
    )
    BUDGET_CHOICES = (
        ("BUDGET","Budget"),
        ("MID_RANGE","Mid-Range"),
        ("lUXURY","Luxury"),


    )
    tour_type=models.CharField(max_length=100,choices=TOUR_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    budget= models.CharField(max_length=100,choices=BUDGET_CHOICES)    
    query = models.TextField()

    def __str__(self):
        return self.name
class Enquire(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone= models.CharField(max_length=100)
    date=models.DateField()
    query = models.TextField()

    def __str__(self):
        return self.name