from django.contrib import admin
from . models import Clients, Ingridients, Orders, Rols
from . models import Mixtures
from . models import Employees
from . models import Vehicles

class ingridientsAdmin(admin.ModelAdmin):
    list_display = ('id','name','agua','arena','grava','cemento','aditivo')

class mixturesAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','agua','arena','grava','cemento','aditivo')
    prepopulated_fields = {'slug': ('name',)}

class rolsAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class employeesAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','slug',
                'phone_number','email','address','rol')
    prepopulated_fields = {'slug': ('firstname',)}

class clientAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','slug',
                'phone_number','email','company')
    prepopulated_fields = {'slug': ('firstname',)}

class orderAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug','client',
                'mixture','measure','destination','date')
    prepopulated_fields = {'slug': ('name',)}

class vehiculesAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug', 'employees')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Ingridients,ingridientsAdmin)
admin.site.register(Mixtures,mixturesAdmin)
admin.site.register(Rols,rolsAdmin)
admin.site.register(Employees,employeesAdmin)
admin.site.register(Clients,clientAdmin)
admin.site.register(Orders,orderAdmin)
admin.site.register(Vehicles,vehiculesAdmin)
