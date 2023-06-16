from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto, Proveedor 
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm, ClientCreationForm, ProveedorForm, CategoriaForm
from django.contrib import messages
from django.core.paginator import Page, Paginator
from django.http import Http404
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
# Create your views here.


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto enviado"
        else:
            data["form"] = formulario
    return render(request, 'app/contacto.html', data)

@permission_required('app.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario =ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/agregar.html', data)


def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render(request, 'app/producto/listar.html', data)

@permission_required('app.change_producto')
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario

    return render(request, 'app/producto/modificar.html', data)


@permission_required('app.delete_producto') 
def eliminar_producto(request, id): 
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eleiminado correctamente")
    return redirect(to="listar_productos")


def registro(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            group = Group.objects.get(name = administrador)
            user.groups.add(administrador)
            login(request, user)
            messages.success(request, "Te has registrado correctamente ")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

# administrador 

def administrador(request):
    productos = Producto.objects.all().count
    data = {
        'productos': productos
    }
    return render(request, 'app/administrador/index.html', data)


def cliente_registro(request):

    data = {
        'form' : ClientCreationForm()
    }

    if request.method == 'POST':
        formulario = ClientCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            cliente = authenticate(username=formulario.cleaned_data["Username"], password=formulario.cleaned_data["password"])
            login(request, cliente)
            messages.success(request, "Te has registrado exitosamente coño")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/cliente_registro.html', data )

def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(proveedores, 5)
        proveedores = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': proveedores,
        'paginator': paginator
    }

    return render(request, 'app/administrador/proveedor/proveedores.html', data)

def agregar_proveedor(request):
    data = {
        'form' : ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Creado correctamente")
            return redirect(to="proveedores")
        data["form"] = formulario
    
    return render(request, 'app/administrador/proveedor/agregar_proveedor.html', data)

def modificar_proveedor(request, id): 
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="proveedores")
        else:
            data["form"] = formulario
    return render(request, 'app/administrador/proveedor/modificar_proveedor.html', data)

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    proveedor.delete()
    messages.success(request, "eleiminado correctamente")
    return redirect(to="proveedores")

def listar_categoria(request):
    categorias = Categoria.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(categorias, 5)
        categorias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': categorias,
        'paginator': paginator
    }
    return render(request, 'app/administrador/categorias.html', data)

def agregar_categoria(request):
    data = {
        'form' : CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria creado correctamente")
            return redirect(to="categorias")
        data["form"] = formulario

    return render(request, 'app/administrador/agregar_categoria.html', data)

def modificar_categoria(request, id):
    categorias = get_object_or_404(Categoria, id_categoria=id)
    data ={
        'form': CategoriaForm(instance=categorias)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categorias)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="categorias")
        data["form"] = formulario
    return render(request, 'app/administrador/modificar_categoria.html', data)

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id_categoria=id)
    categoria.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="categorias")

def carro(request):
    productos = Producto.objects.all()
    
    data = {
        'entity': productos        
    }

    return render(request, 'app/carro.html', data)
