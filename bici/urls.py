from django.conf.urls import url
from django.contrib.auth.views import login_required

from bici.views import ListaBici, VerMapa


urlpatterns = [
    url(r'^listar$', ListaBici.as_view(), name='listar'),
    url(r'^Maps', VerMapa, name="mapa"),
    
]