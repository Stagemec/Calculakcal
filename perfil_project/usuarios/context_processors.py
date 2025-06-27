# seu_app/context_processors.py
from .models import Perfil

def perfil_atual(request):
    if request.user.is_authenticated:
        try:
            perfil = Perfil.objects.get(usuario=request.user)
            return {'perfil_atual_id': perfil.id}
        except Perfil.DoesNotExist:
            return {}
    return {}