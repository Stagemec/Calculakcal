from django.shortcuts import render

# Create your views here.
def index(request):
    """pagina principal Callcall"""
    return render(request, 'Callcall/index.html')