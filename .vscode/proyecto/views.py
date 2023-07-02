from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registrar_Laptop
from .models import vender_Laptop
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q 

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required

def registroVentas(request):
    ventas = vender_Laptop.objects.all()
    return render(request, "registroVentas.html",{
            'ventas': ventas
        })

# Create your views here.

@login_required
def informacionLaptop(request, id):
    laptop = Registrar_Laptop.objects.get(id = id)
    cadena_eliminar = 'proyecto'
    ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar,'')
    ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar,'')
    ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar,'')
    ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar,'')
    return render(request, "informacionLaptop.html",{
        'laptop': laptop,
        'ruta_1': ruta_1,
        'ruta_2': ruta_2,
        'ruta_3': ruta_3,
        'ruta_4': ruta_4,
    })

@login_required
def modificarLaptop(request, id):
    if request.method == 'GET':
        laptop = Registrar_Laptop.objects.get(id = id)
        cadena_eliminar = 'proyecto/static/imagenes/'
        ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar,'')
        ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar,'')
        ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar,'')
        ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar,'')
        return render(request, "modificar_laptop.html",{
            'laptop': laptop,
            'ruta_1': ruta_1,
            'ruta_2': ruta_2,
            'ruta_3': ruta_3,
            'ruta_4': ruta_4,
        })
    else:
        laptop = get_object_or_404(Registrar_Laptop, pk=id)
        laptop.marca = request.POST['marca']
        laptop.modelo = request.POST['modelo']
        laptop.nombre = request.POST['nombre']
        laptop.stock = request.POST['stock']
        laptop.precio = request.POST['precio']
        laptop.pantalla = request.POST['pantalla']
        laptop.teclado = request.POST['teclado']
        laptop.procesador = request.POST['procesador']
        laptop.ram = request.POST['ram']
        laptop.color = request.POST['color']
        laptop.m2 = request.POST['m2']
        laptop.hdd = request.POST['hdd']
        laptop.grafica = request.POST['grafica']
        laptop.descripcion = request.POST['descripcion']
        if 'imagen_1' in request.FILES:
            laptop.imagen_1 = request.FILES['imagen_1']
        if 'imagen_2' in request.FILES:
            laptop.imagen_2 = request.FILES['imagen_2']
        if 'imagen_3' in request.FILES:
            laptop.imagen_3 = request.FILES['imagen_3']
        if 'imagen_4' in request.FILES:
            laptop.imagen_4 = request.FILES['imagen_4']
        laptop.save()
        return redirect("laptops")


def error_404(request, exception):
    return render(request, '403.html', status=404)

@login_required
def laptops(request):
    queryset = request.GET.get("buscar")
    if request.method == 'GET':
        laptops = Registrar_Laptop.objects.all()
        lista_rutas = []
        if queryset:
            laptops = Registrar_Laptop.objects.filter(
            Q(marca__icontains = queryset)|
            Q(descripcion = queryset)
            ).distinct()
        for laptop in laptops:
            ruta_fallida =  str(laptop.imagen_1)
            cadena_eliminar = 'proyecto'
            ruta_correcta = ruta_fallida.replace(cadena_eliminar, '')
            lista_rutas.append(ruta_correcta)
            print(ruta_correcta)
            
        laptops_rutas = zip(laptops, lista_rutas)
        return render(request, "laptops.html",{
            'laptops_rutas': laptops_rutas
        })
    else:
        laptop = Registrar_Laptop.objects.create(
            marca = request.POST['marca'],
            modelo = request.POST['modelo'],
            nombrecli = request.POST['nombre'],
            stock = request.POST['stock'],
            precio = request.POST['precio'],
            pantalla = request.POST['pantalla'],
            teclado = request.POST['teclado'],
            procesador = request.POST['procesador'],
            ram = request.POST['ram'],
            color = request.POST['color'],
            m2 = request.POST['m2'],
            hdd = request.POST['hdd'],
            grafica = request.POST['grafica'],
            descripcion = request.POST['descripcion'],
            imagen_1 = request.FILES['imagen_1'],
            imagen_2 = request.FILES['imagen_2'],
            imagen_3 = request.FILES['imagen_3'],
            imagen_4 = request.FILES['imagen_4'])
        messages.success(request, f"¡La laptop {laptop.nombre} ha sido registrada exitosamente!")
        return redirect("laptops")
    
@login_required
def venderLaptop(request, id=None):
    if request.method == 'GET':
        laptop = Registrar_Laptop.objects.get(id = id)
        cadena_eliminar = 'proyecto/static/imagenes/'
        ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar,'')
        ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar,'')
        ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar,'')
        ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar,'')
        return render(request, "venderlaptop.html",{
            'laptop': laptop,
            'ruta_1': ruta_1,
            'ruta_2': ruta_2,
            'ruta_3': ruta_3,
            'ruta_4': ruta_4,
        })
        
    else:
        laptop = vender_Laptop.objects.create(
            marca = request.POST['marca'],
            modelo = request.POST['modelo'],
            cantidad = request.POST['cantidad'],
            precio = request.POST['precio'],
            fecha = request.POST['fecha'],
            cliente = request.POST['cliente'],
            direccion = request.POST['direccion'],
            ci = request.POST['ci'],
            telefono = request.POST['telefono'],)
        messages.success(request, f"¡La venta ha sido registrada exitosamente!")
        return redirect("laptops")
        

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return render(request, 'login.html')
            else:
                login(request, user)
                return redirect("index")
        except:
            return redirect("signin")


def signout(request):
    logout(request)
    return redirect("index")

