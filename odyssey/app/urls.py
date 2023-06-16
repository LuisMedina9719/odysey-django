from django.contrib.messages import api
from django.urls import path
from .views import eliminar_proveedor, home, contacto, agregar_producto, listar_productos, modificar_producto,eliminar_producto, \
    registro, administrador, cliente_registro, listar_proveedor, agregar_proveedor, modificar_proveedor, listar_categoria, agregar_categoria,  \
        modificar_categoria, eliminar_categoria, carro
        


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('cliente-registro/', cliente_registro, name="cliente_registro") ,
    # administrador
    path('administrador/', administrador, name="administrador"),
    path('registro/', registro, name="registro"),
    path('proveedores/', listar_proveedor, name="proveedores"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('listar-categoria/', listar_categoria, name="categorias"),
    path('agregar-categoria', agregar_categoria, name="agregar_categoria"),
    path('modificar-categoria/<id>/', modificar_categoria, name="modificar_categoria"),
    path('eliminar-categoria/<id>/', eliminar_categoria, name="eliminar_categoria"),
    # carro
    path('carro',carro,name="mostrar_carro"),

]
