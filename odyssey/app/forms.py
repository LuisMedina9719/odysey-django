from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Contacto, Producto, Proveedor, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups'

class ClientCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
        
class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
