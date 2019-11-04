# Django
from django.http import HttpResponse
import json
# Utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Tiempo del servidor {now}'.format(
        now=str(now)
    ))


def sort_integers(request):
    # Obtener la lista de numeros, ordenarla e imprimirla en formato json
    #Aqui tenemos que recorrer cada elemnto de numbers
    numbers =[ int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message': 'Integers sorted'

    }
    #Dumps traduce a json
    return HttpResponse(json.dumps(data),
                        content_type='application/json'
                        )


def say_hi(request,name,age):

    if age < 12:
        message = 'Sorry {}, No tienes acceso'.format(name)
    else:
        message = 'Hello,{} Bienvenido'.format(name)

    return HttpResponse(message)