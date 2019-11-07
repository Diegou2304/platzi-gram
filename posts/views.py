

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
posts = [

    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Diego Uribe',
            'picture':'https://scontent.fvvi1-1.fna.fbcdn.net/v/t1.0-9/41366332_10209679944274244_8762378409402695680_n.jpg?_nc_cat=103&_nc_oc=AQl4kG3y2tg1ds0HjYo9xGIO2CN5gSduPbVjDPyQp-aZ2QutPUYbTJJNi4ETWtYSEpveamohFlrC57Mn9hOyHCKe&_nc_ht=scontent.fvvi1-1.fna&oh=1389ed7341baad96b04329c844544063&oe=5E488F2F',


        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo':     'https://webgenery-images.s3.eu-west-1.amazonaws.com/5BC458428821C972555846/espace_dynamique/1/7-A.jpg',



    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'Angel Wayar',
            'picture': 'https://scontent.fvvi1-1.fna.fbcdn.net/v/t1.0-9/66394823_10220433009474484_6584010660894474240_n.jpg?_nc_cat=110&_nc_oc=AQnOl0fZiOA0MCZQcNWhFSAn_BiTJ-akcyA7fKwBAzaEEmkcQDiRB_DG7284SbxwM6nubp5hgf6N4FYVo0wo4FWa&_nc_ht=scontent.fvvi1-1.fna&oh=308523b7b85d2897859db513555655c0&oe=5E5FE56A'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://ichef.bbci.co.uk/news/660/cpsprodpb/27F1/production/_105952201_9372.jpg'

    },


]

def list_posts(request):

    #Recibe contextos
    return render(request,'feed.html',{'posts': posts})
