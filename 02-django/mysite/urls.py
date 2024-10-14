from django.contrib import admin
from django.urls import path
# from myapp import views
import myapp.views

urlpatterns = [
    # url principal
    path('', myapp.views.index, name='index'),
    
    # url de inicio (usando una misma view)
    path('inicio', myapp.views.index, name='index'),
    
    # vista basada en funcion
    path('mivista/', myapp.views.mi_vista, name='mi_vista'),
    
    # viiw prueba de backend
    path('api/vista/', myapp.views.mi_vista_api, name='mi_vista_api')
]
