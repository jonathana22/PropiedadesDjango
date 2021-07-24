from django.urls import path
from .views import home, galeria, contacto, datos, Agregar, construccion
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/<int:id>/', views.galeria, name="galeria"),
    path('datos/', datos, name="datos"),
    path('Agregar/', Agregar, name="Agregar"),
    path('construccion/', construccion, name="construccion"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
