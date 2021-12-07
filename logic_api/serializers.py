from rest_framework import serializers
from .models import Clients, Ingridients, Rols, Orders
from .models import Mixtures
from .models import Employees
from .models import Vehicles

#Ingridients
class ingridientsSerializer(serializers.ModelSerializer):
  
   class Meta:
       model=Ingridients
       fields= '__all__'
#       fields=('name')

#Mixtures
class mixturesSerializer(serializers.ModelSerializer):
  
   class Meta:
       model=Mixtures
       fields= '__all__'
#       fields=('name')
 
#Rols
class rolsSerializer(serializers.ModelSerializer):
   
   class Meta:
       model=Rols
       fields= '__all__'
#       fields=('name')
 
class employeesSerializer(serializers.ModelSerializer):
   rol = serializers.StringRelatedField()
   class Meta:
       model=Employees
       fields= '__all__'
#       fields=('name')

#Employees
class employeesCUDSerializer(serializers.ModelSerializer):
   
   class Meta:
       model=Employees
       fields= '__all__'
#       fields=('name')
 
class clientsSerializer(serializers.ModelSerializer):
  
   class Meta:
       model=Clients
       fields= ('id','firstname','lastname',
                    'phone_number','email','company')
#       fields=('name')
 

#Orders
class ordersSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    mixture = serializers.StringRelatedField()
    class Meta:
       model=Orders
       fields= ('id','name','slug','client',
                    'mixture','measure','destination','date')
    
class ordersCUDSerializer(serializers.ModelSerializer):
   class Meta:
       model=Orders
       fields= ('id','name','slug','client',
                    'mixture','measure','destination','date')


#Vehicules
class vehiclesSerializer(serializers.ModelSerializer):
   employees = serializers.StringRelatedField()
   class Meta:
       model=Vehicles
       fields= '__all__'
#       fields=('name')

class vehiclesCUDSerializer(serializers.ModelSerializer):
   class Meta:
       model=Vehicles
       fields= '__all__'
#       fields=('name')
