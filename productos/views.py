from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.
def inicio(request):
    productos=Producto.objects.all().order_by('marca')
    return render(request, 'index.html',{"productos":productos})

def BuscarProducto(request):
    filtro=request.POST['filtro']
    productos=Producto.objects.filter(categoria__contains=filtro)
    if len(productos)>0:
        return render(request,'index.html',{"productos":productos})
    else:
        productos=Producto.objects.filter(marca__contains=filtro)
        return render(request,'index.html',{"productos":productos})


def EliminarProducto(request,marca,categoria):
    producto=Producto.objects.get(marca=marca,categoria=categoria)
    producto.delete()
    return redirect('/')


def NuevoProducto(request): #para renderizar la pagina de formulario de nuevo producto
    return render(request,'nuevoprodu.html')

def CrearProducto(request):
    marca=request.POST['crearmarca']
    categoria=request.POST['crearcategoria']
    precio=request.POST['crearprecio']
    producto=Producto.objects.create(marca=marca,categoria=categoria,precio=precio)
    producto.save()
    print(marca)
    return redirect('/')

#falta editar y estaria el CRUD

def EdicionProducto(request,marca, categoria):
    producto=Producto.objects.get(marca=marca,categoria=categoria)
    return render (request,'editarprodu.html',{"producto":producto})

def EditarProducto(request):
    marca=request.POST['editarmarca']
    categoria=request.POST['editarcategoria']
    precionuevo=request.POST['editarprecio']
    
    producto=Producto.objects.get(marca=marca,categoria=categoria)
    producto.precio=precionuevo
    producto.save()

    return redirect('/')

