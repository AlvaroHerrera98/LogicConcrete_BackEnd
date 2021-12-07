from django.db.models.lookups import In
from django.shortcuts import render
 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, AllowAny, BasePermission, DjangoModelPermissions, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from . models import Clients, Ingridients, Orders, Rols
from . models import Mixtures
from . models import Employees
from . models import Vehicles
from . serializers import clientsSerializer, employeesCUDSerializer, ingridientsSerializer, ordersCUDSerializer, ordersSerializer, rolsSerializer, vehiclesCUDSerializer
from . serializers import mixturesSerializer
from . serializers import employeesSerializer
from . serializers import vehiclesSerializer

class authorizedUser(BasePermission):
    message = 'Solo usuarios autorizados puede hacer cambios'

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        return obj.firstname == request.user

#Ingridients
class ingredienteList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ingridientsSerializer
    queryset=Ingridients.objects.all()

class ingredineteDetails(generics.RetrieveAPIView):
    serializer_class = ingridientsSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Orders, slug=item)

class editIngridients(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ingridientsSerializer
    queryset=Ingridients.objects.all()



#Mixtures
class mixturesList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = mixturesSerializer
    queryset= Mixtures.objects.all()

class mixturesDetails(generics.RetrieveAPIView):
    serializer_class = mixturesSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Mixtures, slug=item)

class createMixtures(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = mixturesSerializer
    queryset= Mixtures.objects.all()


class editMixtures(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = mixturesSerializer
    queryset= Mixtures.objects.all()


class deleteMixtures(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = mixturesSerializer
    queryset= Mixtures.objects.all()


class adminMixturesDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = mixturesSerializer
    queryset= Mixtures.objects.all()



#Rols
class rolsList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = rolsSerializer
    queryset= Rols.objects.all()

class rolsDetails(generics.RetrieveAPIView):
    serializer_class = rolsSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Rols, slug=item)



#Employees
class employeesList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = employeesSerializer
    queryset= Employees.objects.all()

class employeesDetails(generics.RetrieveAPIView):
    serializer_class = employeesSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Employees, slug=item)

class createEmployees(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = employeesCUDSerializer
    queryset= Employees.objects.all()

class editEmployees(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = employeesCUDSerializer
    queryset= Employees.objects.all()

class deleteEmployees(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = employeesCUDSerializer
    queryset= Employees.objects.all()

class adminEmployeesDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = employeesCUDSerializer
    queryset= Employees.objects.all()


#Clients
class clientsList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = clientsSerializer
    queryset= Clients.objects.all()

class clientsDetails(generics.RetrieveAPIView):
    serializer_class = clientsSerializer
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Clients, slug=item)

class createClient(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = clientsSerializer
    queryset= Clients.objects.all()

class editClient(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = clientsSerializer
    queryset= Clients.objects.all()

class deleteClient(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = clientsSerializer
    queryset= Clients.objects.all()

class adminClientDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = clientsSerializer
    queryset= Clients.objects.all()



#Vehicules
class vehiculesList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = vehiclesSerializer
    queryset= Vehicles.objects.all()

class vehiculesDetails(generics.RetrieveAPIView):
    serializer_class = vehiclesSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Vehicles, slug=item)

class createVehicules(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = vehiclesCUDSerializer
    queryset= Vehicles.objects.all()

class editVehicules(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = vehiclesCUDSerializer
    queryset= Vehicles.objects.all()

class deleteVehicules(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = vehiclesCUDSerializer
    queryset= Vehicles.objects.all()

class adminVehiculesDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = vehiclesCUDSerializer
    queryset= Vehicles.objects.all()


#Orders
class ordersList (generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ordersSerializer
    queryset= Orders.objects.all()

class ordersDetails(generics.RetrieveAPIView):
    serializer_class = ordersSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Orders, slug=item)

class createOrders(generics.CreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ordersCUDSerializer
    queryset= Orders.objects.all()

class editOrders(generics.UpdateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ordersCUDSerializer
    queryset= Orders.objects.all()

class deleteOrders(generics.RetrieveDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ordersCUDSerializer
    queryset= Orders.objects.all()

class adminOrdersDetail(generics.RetrieveAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = ordersCUDSerializer
    queryset= Orders.objects.all()























# class ordersList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=ordersSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Orders, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Orders.objects.all()

# class ingridientsList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=ingredientsSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Ingredients, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Ingredients.objects.all()

# class mixturesList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=mixturesSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Mixtures, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Mixtures.objects.all()

# class rolsList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=rolsSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Rols, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Rols.objects.all()

# class employeesList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=employeesSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Employees, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Employees.objects.all()

# class clientsList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=clientsSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Clients, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Clients.objects.all()

# class vehiculesList(viewsets.ModelViewSet):
#     permission_classes = [DjangoModelPermissions]
#     serializer_class=vehiclesSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Vehicles, slug=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return Vehicles.objects.all()