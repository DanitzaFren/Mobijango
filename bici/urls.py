from django.conf.urls import url
from django.contrib.auth.views import login_required

from bici.views import ListaBici, VerMapa,Scaner


urlpatterns = [
    url(r'^listar$', ListaBici.as_view(), name='listar'),
    url(r'^Maps', VerMapa, name="mapa"),
    url(r'^Scaneer', Scaner, name="sca"),
    
]