from django.urls import path
from . import views
from django.conf.urls import handler404
urlpatterns = [
    path('', views.index, name="index"),
    path('laptops/', views.laptops, name="laptops"),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name="signin"),
    path('informacionLaptop/<int:id>',views.informacionLaptop, name = "informacionLaptop"),
    path('modificarLaptop/<int:id>',views.modificarLaptop, name = "modificarLaptop"),
    path('venderLaptop/<int:id>',views.venderLaptop, name = "venderLaptop"),
    path('registroVentas/',views.registroVentas, name = "registroVentas"),

]


handler404 = 'proyecto.views.error_404'