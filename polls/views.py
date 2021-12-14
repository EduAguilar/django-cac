from django.shortcuts import render
from django.http import HttpResponse, response
from polls.models import Music
import json

# Create your views here.
def index(resquest):
    #return render(resquest, 'polls/index.html')
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#Definimos nuestro CRUD, Create, Read, Update, Delete
def read(resquest, id):
    myMusic = Music.objects.get(id=id)
    #myMusicJSON = json.load(myMusic)

    return HttpResponse(" %s." % myMusic)

def delete(resquest, id):
    myMusic = Music.objects.get(id=id)
    myMusic.delete()
    return HttpResponse("Music with id: %s delete." %id)

def create(resquest):
    myMusic = Music(artist="My artist", album = "My album", genre="My genero")
    myMusic.save()
    return HttpResponse("Music with id: %s created." %myMusic.id)


def update(resquest, id):

    myResponse= HttpResponse("You must use POST Method")

    if resquest.method == 'POST':
        myMusic = Music.objects.get(id=id)
        myMusic.artist = resquest.POST.get('artist')
        myMusic.album = resquest.POST.get ('album')
        myMusic.genre = resquest.POST.get ('genre')
        myMusic.save()
        myResponse = HttpResponse("Music with id: %s update")
    return myResponse
    