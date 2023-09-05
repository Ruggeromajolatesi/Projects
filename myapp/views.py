from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404 #questa FUN suggerisce errore della pg
#from django.http import HttpResponse modo1/modo2 from myapp import views
#from myapp import views

# Create your views here.
def index(request):
    return HttpResponse('Index page')
def hello(request, username):
    print(username)
    #print(type(id))
    return HttpResponse('<h1>Hello %s</h1>' % username) 

# per concatenare 'username con hello aggiungo '%s' poi % username, oppure ID-- IN BASE A COSA SPECIFICO NEL PATH( se si tratta di STR INT etc.etc.) 
#possono essere ricevuti vari parametri
#posso anche ottenere risultati di operazioni numeriche

def project(request):
    projects = list(Project.objects.values()) #ottengo una lista di progetti#per convertire in un json devo cambiare in una lista PY [cambio da:Project.objects.ALL a Project.objects.VALUES]
    return JsonResponse(projects, safe= False)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe= False)


def task(request, id): #tile
    #task = Task.objects.get(id=id) #passo il parametro che voglio ottenere, cercandolo mediante il parametro che ho / (tile=title)
    get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)