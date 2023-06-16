from django.contrib import admin
from .models import Producto, Contacto, Proveedor

# Register your models here.


admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Contacto)

