from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registrar_Laptop
from .models import vender_Laptop, crear_factura
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q 
from django.db.models import F, ExpressionWrapper, FloatField
from django.shortcuts import render
from .models import vender_Laptop, registrar_usuario
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')        
def usuarios(request):
    usuarios = registrar_usuario.objects.all()
    return render(request, "usuarios.html",{'usuarios':usuarios})


@login_required
def factura(request):
    return render(request, "factura.html")

@user_passes_test(lambda u: u.is_superuser, login_url='/403/')        

def usuarios(request):
    usuarios = registrar_usuario.objects.all()
    return render(request, "usuarios.html",{'usuarios':usuarios})

def registro(request):
    if request.method == 'POST':
        nombemp = request.POST.get('nombemp')
        ciemp = request.POST.get('ciemp')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        confirmar_contraseña = request.POST.get('confirmar_password')

        errors_dict = {}

        # Verificar si los datos ya están registrados
        if registrar_usuario.objects.filter(nombemp=nombemp).exists():
            errors_dict['nombemp'] = 'El nombre de empleado ya está registrado.'
        if registrar_usuario.objects.filter(ciemp=ciemp).exists():
            errors_dict['ciemp'] = 'El CI proporcionado ya está asociado con una cuenta existente.'
        if registrar_usuario.objects.filter(usuario=usuario).exists():
            errors_dict['usuario'] = 'El nombre de usuario proporcionado ya está asociado con una cuenta existente.'

        if password != confirmar_contraseña:
            errors_dict['password'] = 'La confirmación de contraseña no coincide con la contraseña ingresada.'

        if len(errors_dict) == 0:
            nuevo_usuario = registrar_usuario.objects.create(nombemp=nombemp, ciemp=ciemp, usuario=usuario, password=password)
            nuevo_usuario = User.objects.create_user(username=usuario, password=password)
            nuevo_usuario.save()
            messages.success(request, f"¡El usuario ha sido registrada exitosamente!")
            return redirect('registro')

        context = {
            'errors_dict': errors_dict,
            'nombemp': nombemp,
            'ciemp': ciemp,
            'usuario': usuario
        }
        return render(request, "registro.html", context)

    return render(request, "registro.html")

@login_required
def registroVentas(request):
    ventas = vender_Laptop.objects.annotate(
        total=ExpressionWrapper(F('cantidad') * F('precio'), output_field=FloatField())
    ).order_by('fecha')
    return render(request, "registroVentas.html",{
        'ventas': ventas
    })

@login_required
def registroFacturas(request):
    facturas = crear_factura.objects.all()
    return render(request, "registroFacturas.html",{
            'facturas': facturas
        })


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')
def reporteVentas(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        ventas = vender_Laptop.objects.filter(fecha__range=[fecha_inicio, fecha_fin])

        no_ventas = False
        if not ventas.exists():
            no_ventas = True

        ventas_suma = {}
        for venta in ventas:
            if venta.marca in ventas_suma:
                ventas_suma[venta.marca]['cantidad'] += venta.cantidad
                ventas_suma[venta.marca]['precio'] += venta.precio
            else:
                ventas_suma[venta.marca] = {
                    'cantidad': venta.cantidad,
                    'precio': venta.precio
                }

        context = {
            'ventas': ventas_suma,
            'no_ventas': no_ventas,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin
        }
    else:
        context = {}

    return render(request, "reporte_ventas.html", context)



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
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')        
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
        messages.success(request, f"¡La laptop {laptop.nombre} ha sido modificada exitosamente!")
        return redirect("modificarLaptop", id=id)


def error_404(request, exception):
    return render(request, '403.html', status=404)

@login_required
def laptops(request):
    queryset = request.GET.get("buscar")
    if request.method == 'GET':
        laptops = Registrar_Laptop.objects.all()
        lista_rutas = []
        if queryset:
            if Registrar_Laptop.objects.filter(
            Q(marca__icontains = queryset)):
                laptops = Registrar_Laptop.objects.filter(
                Q(marca__icontains = queryset)|
                Q(descripcion = queryset)
                ).distinct()
            else:
                messages.add_message(request, messages.ERROR, "No se encontro ese resultado")
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
            nombre = request.POST['nombre'],
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
        laptop = Registrar_Laptop.objects.get(id=id)
        cadena_eliminar = 'proyecto/static/imagenes/'
        ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar, '')
        ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar, '')
        ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar, '')
        ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar, '')
        return render(request, "venderlaptop.html", {
            'laptop': laptop,
            'ruta_1': ruta_1,
            'ruta_2': ruta_2,
            'ruta_3': ruta_3,
            'ruta_4': ruta_4,
        })

    else:
        laptop = Registrar_Laptop.objects.get(id=id)
        cantidad_vendida = int(request.POST['cantidad'])
        if cantidad_vendida > laptop.stock:
            messages.error(request, f"No hay suficiente stock para vender {cantidad_vendida} unidades.")
            return redirect('vender_laptop', id=laptop.id)
        else:
            laptop.stock -= cantidad_vendida
            laptop.save()
            laptop = vender_Laptop.objects.create(
                marca=request.POST['marca'],
                modelo=request.POST['modelo'],
                cantidad=cantidad_vendida,
                precio=request.POST['precio'],
                fecha=request.POST['fecha'],
                cliente=request.POST['cliente'],
                direccion=request.POST['direccion'],
                ci=request.POST['ci'],
                telefono=request.POST['telefono'],
            )
            messages.add_message(request, messages.WARNING, f"¡La venta ha sido registrada exitosamente!")
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



@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/403/')
def eliminarUsuario(request, id):
    usuario = get_object_or_404(registrar_usuario, id=id)
    usuario.delete()
    return redirect("usuarios")