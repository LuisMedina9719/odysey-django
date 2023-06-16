from django.urls import path
from .import views

app_name="carro"


urlpatterns = [

    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar_carro"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar_carro"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar_carro"),
    path("limpiar/", views.limpiar_carro, name="limpiar_carro"),
    path("sumar/<int:producto_id>/", views.sumar_carro, name="sumar_carro")

    

]
