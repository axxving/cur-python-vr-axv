from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
#  ?
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Inicio.")

def mi_vista(request):
    return HttpResponse("Hola, esta es mi primera vista en django.")

# Views probadas en backend
@csrf_exempt
def mi_vista_api(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Esta es una solicitud GET"})

    elif request.method == 'POST':
        data = request.POST.get('data', 'No se envió data')
        return JsonResponse({"message": "Esta es una solicitud POST", "data": data})

    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)




# View para practica con url com parametros
@csrf_exempt
def vista_parametros_url(request, id, name):
    if request.method == 'GET':
        return JsonResponse({
            "message": "Esta es una solicitud GET",
            "id": id,
            "name": name
        })

    elif request.method == 'POST':
        data = request.POST.get('data', 'No se envió data')
        return JsonResponse({
            "message": "Esta es una solicitud POST",
            "id": id,
            "name": name,
            "data": data
        })

    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)




@csrf_exempt
def vista_parametros_opcionales(request, id=None, name=None):
    if request.method == 'GET':
        return JsonResponse({
            "message": "Esta es una solicitud GET",
            "id": id if id else "No se proporciono un id",
            "name": name if name else "No se proporciono un nombre"
        })
    
    elif request.method == 'POST':
        data = request.POST.get('data', 'No se envió data')
        return JsonResponse({
            "message": "Esta es una solicitud POST",
            "id": id if id else "No se proporciono un id",
            "name": name if name else "No se proporciono un nombre",
            "data": data
        })
    
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)