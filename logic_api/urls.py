from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import adminClientDetail, adminEmployeesDetail, adminMixturesDetail, adminOrdersDetail, adminVehiculesDetail, createClient, createEmployees, createMixtures, createOrders, deleteClient, deleteEmployees, deleteMixtures, deleteOrders, deleteVehicules, editClient, editEmployees, editIngridients, editMixtures, editOrders, editVehicules, mixturesList, ingredienteList, ordersList, clientsList, employeesList, rolsList, vehiculesList, createVehicules

app_name = 'logic_api'

# router = DefaultRouter()
# router.register('mixtures', mixturesList, basename='mixtures')
# router.register('ingridients', ingridientsList, basename='ingridients')
# router.register('employees', employeesList, basename='employees')
# router.register('clients', clientsList, basename='clients')
# router.register('rols', rolsList, basename='rols')
# router.register('orders', ordersList, basename='orders')
# router.register('vehicules', vehiculesList, basename='vehicules')

# urlpatterns = router.urls

urlpatterns = [
    #Mixtures
    path('mixtures/', mixturesList.as_view()),
    path('mixtures-auth/', include('rest_framework.urls', namespace='rest_framework1')),
    path('mixtures/create/', createMixtures.as_view(), name='createmixtures'),
    path('mixtures/edit/mixturesdetail/<int:pk>/', adminMixturesDetail.as_view(), name='adminmixturesdetail'),
    path('mixtures/edit/<int:pk>/', editMixtures.as_view(), name='editmixtures'),
    path('mixtures/delete/<int:pk>/', deleteMixtures.as_view(), name='editmixtures'),

    #Ingridients
    path('ingridients/', ingredienteList.as_view()),
    path('ingridients-auth/', include('rest_framework.urls', namespace='rest_framework2')),
    path('ingridients/edit/<int:pk>/', editIngridients.as_view(), name='editingridients'),

    #Employees
    path('employees/', employeesList.as_view()),
    path('employees-auth/', include('rest_framework.urls', namespace='rest_framework3')),
    path('employees/create/', createEmployees.as_view(), name='createemployees'),
    path('employees/edit/employeesdetail/<int:pk>/', adminEmployeesDetail.as_view(), name='adminemployeesdetail'),
    path('employees/edit/<int:pk>/', editEmployees.as_view(), name='editemployees'),
    path('employees/delete/<int:pk>/', deleteEmployees.as_view(), name='editemployees'),
    
    #Clients
    path('clients/', clientsList.as_view()),
    path('clients/', include('rest_framework.urls', namespace='rest_framework4')),
    path('clients/create/', createClient.as_view(), name='createclient'),
    path('clients/edit/clientdetail/<int:pk>/', adminClientDetail.as_view(), name='adminclientdetail'),
    path('clients/edit/<int:pk>/', editClient.as_view(), name='editclient'),
    path('clients/delete/<int:pk>/', deleteClient.as_view(), name='editclient'),

    #Rols
    path('rols/', rolsList.as_view()),
    path('rols-auth/', include('rest_framework.urls', namespace='rest_framework5')),

    #Orders
    path('orders/', ordersList.as_view()),
    path('orders-auth/', include('rest_framework.urls', namespace='rest_framework6')),
    path('orders/create/', createOrders.as_view(), name='createorder'),
    path('orders/edit/orderdetail/<int:pk>/', adminOrdersDetail.as_view(), name='adminorderdetail'),
    path('orders/edit/<int:pk>/', editOrders.as_view(), name='editorder'),
    path('orders/delete/<int:pk>', deleteOrders.as_view(), name='editorder'),

    #Vehicules
    path('vehicules/', vehiculesList.as_view()),
    path('vehicules-auth/', include('rest_framework.urls', namespace='rest_framework7')),
    path('vehicules/create/', createVehicules.as_view(), name='createorder'),
    path('vehicules/edit/vehiculesdetail/<int:pk>/', adminVehiculesDetail.as_view(), name='adminorderdetail'),
    path('vehicules/edit/<int:pk>/', editVehicules.as_view(), name='editorder'),
    path('vehicules/delete/<int:pk>', deleteVehicules.as_view(), name='editorder'),
]
