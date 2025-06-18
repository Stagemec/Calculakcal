from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """pagina principal Callcall"""
    return render(request, 'Callcall/index.html')

def topics(request):
    """mostra todos os asssuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'Callcall/topics.html', context)