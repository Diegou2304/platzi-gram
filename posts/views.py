

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
posts = [

    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://webgenery-images.s3.eu-west-1.amazonaws.com/5BC458428821C972555846/espace_dynamique/1/7-A.jpg',


    },
    {
        'name': 'Via Lactea',
        'user': 'Diego Uribe',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://ichef.bbci.co.uk/news/660/cpsprodpb/27F1/production/_105952201_9372.jpg',

    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'TheSpinArtist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://cflvdg.avoz.es/default/2016/04/24/0012_201604LA24C2F1jpg/Foto/LA24C2F1.jpg',

    },



]

def list_posts(request):
    content = []
    for post in posts:
        #El format post es para descifrar el diccionario de manera mas rápida
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        
        
        """.format(**post))

    return HttpResponse('<br>'.join(content))
