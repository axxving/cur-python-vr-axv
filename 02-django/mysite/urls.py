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
    path('api/vista/', myapp.views.mi_vista_api, name='mi_vista_api'),
    
    # Vista de la view con parametros en la URL
    path('api/vista/<int:id>/<str:name>/', myapp.views.vista_parametros_url, name='vista_parametros_url'),
    
    # Vista de la viw con parametros opcionales
    
    # Sin parametros
    path('api/vista/opcionales/', myapp.views.vista_parametros_opcionales, name='vista_parametros_opcionales'),
    
    # Con un id opcional
    path('api/vista/opcionales/<int:id>/', myapp.views.vista_parametros_opcionales, name='vista_parametros_opcionales_id'),
    
    # Con id y name opcionales
    path('api/vista/opcionales/<int:id>/<str:name>/', myapp.views.vista_parametros_opcionales, name='vista_parametros_opcionales_id_name')
]
