from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify 
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

DEFAULT_VALUE = 0
DEFAULT_NAME= 'NONE'
class Ingridients(models.Model):
   name=models.CharField(max_length=50, default=DEFAULT_NAME)
   agua=models.IntegerField(default=DEFAULT_VALUE)
   arena=models.IntegerField(default=DEFAULT_VALUE)
   grava=models.IntegerField(default=DEFAULT_VALUE)
   cemento=models.IntegerField(default=DEFAULT_VALUE)
   aditivo=models.IntegerField(default=DEFAULT_VALUE)
 
   def __str__(self):
       return self.name
 

class Mixtures(models.Model):
   name=models.CharField(max_length=50, default=DEFAULT_NAME)
   slug=models.SlugField(max_length=250, null=True, unique=True)
   agua=models.FloatField(default=DEFAULT_VALUE)
   arena=models.FloatField(default=DEFAULT_VALUE)
   grava=models.FloatField(default=DEFAULT_VALUE)
   cemento=models.FloatField(default=DEFAULT_VALUE)
   aditivo=models.FloatField(default=DEFAULT_VALUE)

   def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Mixtures, self).save(*args, **kwargs)
   
   def __str__(self):
       return self.name
 
class Rols(models.Model):
   name=models.CharField(max_length=50)
   
   def __str__(self):
       return self.name
 
DEFAULT_ROL = 0
class Employees(models.Model):
   firstname=models.CharField(max_length=50)
   lastname=models.CharField(max_length=50)
   slug=models.SlugField(max_length=250, null=True, unique=True)
   phone_number=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
   email=models.EmailField()
   address=models.CharField(max_length=50)
   rol=models.ForeignKey(Rols, default= DEFAULT_ROL, on_delete=CASCADE)

   def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Employees, self).save(*args, **kwargs)
 
   def __str__(self):
       return self.firstname
 
class Clients(models.Model):
   firstname=models.CharField(max_length=50)
   lastname=models.CharField(max_length=50)
   slug=models.SlugField(max_length=250,null=True, unique=True)
   phone_number=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
   email=models.EmailField()
   company=models.CharField(max_length=50)

   def save(self, *args, **kwargs):
        self.slug = slugify(self.firstname)
        super(Clients, self).save(*args, **kwargs)
 
   def __str__(self):
       return self.firstname
 
class Orders(models.Model):
   DEFAULT_NAME='NONE'
   name=models.CharField(max_length=50, default=DEFAULT_NAME)
   slug=models.SlugField(max_length=250, null=True, unique=True)
   client=models.ForeignKey(Clients, on_delete=CASCADE)
   mixture=models.ForeignKey(Mixtures, on_delete=CASCADE)
   measure=models.IntegerField()
   destination=models.CharField(max_length=50)
   date=models.DateField()

   def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Orders, self).save(*args, **kwargs)
 
   def __str__(self):
       return self.name
   
#    @property
#    def client_firstname(self):
#        return self.client.firstname

#    def mixture_name(self):
#        return self.mixture.name
  
class Vehicles(models.Model):
   name=models.CharField(max_length=50)
   slug=models.SlugField(max_length=250, null=True, unique=True)
   employees=models.ForeignKey(Employees,related_name='employee', on_delete=models.CASCADE,)

   def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Vehicles, self).save(*args, **kwargs)

   def __str__(self):
       return self.name