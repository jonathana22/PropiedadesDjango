from django.shortcuts import render, get_object_or_404
from .models import Propiedad, Galeria
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    propiedades = Propiedad.objects.all()
    data = {'propiedades':propiedades}
    if request.method=="POST":
        subject=request.POST["txtnombre"]
        message=request.POST["txtemail"]+ " " + request.POST["txtmensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["cristianpezoa.ar@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    return render(request,'core/home.html', data)



def galeria(request, id):
    propiedad = get_object_or_404(Propiedad, id=id)
    foto_galeria = Galeria.objects.filter(propiedad=propiedad)
    data = {
        'propiedad':propiedad,
        'foto_galeria':foto_galeria
        }
    return render(request, 'core/galeria.html', data)


def contacto(request):
    if request.method=="POST":
        subject=request.POST["txtnombre"]
        message=request.POST["txtemail"]+ " " + request.POST["txtmensaje"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["cristianpezoa.ar@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
    return render(request, 'core/contacto.html')


def datos(request):
    return render(request, 'core/datos.html')

def Agregar(request):
    propiedad = Propiedad.objects.all()
    data = {'propiedad':propiedad}
    """ if request.POST:
        propiedad = Propiedad()
        propiedad.nombre = request.POST.get('txtnombre')
        propiedad.tipo = request.POST.get('txtTipo')
        propiedad.operacion = request.POST.get('txtOperacion')
        propiedad.superficie = int(request.POST.get('txtSuperficie'))
        propiedad.habitaciones = int(request.POST.get('txtHabitaciones'))
        propiedad.banno = int(request.POST.get('txtBannos'))
        propiedad.ubicacion = request.POST.get('txtUbicacion')
        propiedad.precio = int(request.POST.get('txtPrecio'))
        propiedad.descripcion = request.POST.get('txtDescripcion')
        propiedad.imgane = request.FILES.GET('imagen')
    try:
        propiedad.save() """

    return render(request, 'core/Agregar.html')
  

def construccion(request):
    return render(request, 'core/construccion.html')