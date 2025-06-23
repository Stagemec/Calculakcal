from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    """pagina principal Callcall"""
    return render(request, 'Callcall/index.html')

def topics(request):
    """mostra todos os asssuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'Callcall/topics.html', context)

def topic(request, topic_id):
    """mostra um unico assunto e todas as entyradas."""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries}
    return render(request, 'Callcall/topic.html', context)

def new_topic(request):
    """"adiciona um novo assunto"""
    if request.method != 'POST':
        # nenhum dado subimetido; criar um formulario em branco
        form = TopicForm()
    else:
        # Dados de Post submetidos; processa dos daos 
        form = TopicForm(reversed.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context={'form' : form}
    return render(request, 'Callcall/new_topic.html' , context)

def new_entry(request, topic_id):
    """"Acrescenta uma nova entrada para um assunto especifico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #nenhum dado subimetido cria um formulario em branco
        form = EntryForm()

    else:
        #Dados de POST subimetido; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            newentry = form.save(comit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        context = {'topic':topic, 'form':form}
        return render(request, 'Callcall/new_entry.html', context)