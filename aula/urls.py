from django.conf.urls import url
from .views import CreateAula, ListAula, EditAula, DeleteAula
from .views import CreateIngrediente, ListIngrediente, EditIngrediente, DeleteIngrediente
from .views import CreateAulaIngrediente, ListAulaIngrediente, EditAulaIngrediente, DeleteAulaIngrediente

urlpatterns = [
    url(r'^aula/create/$', CreateAula.as_view(), name='create'),
    url(r'^aula/list/$', ListAula.as_view(), name='list'),
    url(r'^aula/edit/(?P<id>[0-9]+)$', EditAula.as_view(), name='edit'),
    url(r'^aula/delete/(?P<id>[0-9]+)$', DeleteAula.as_view(), name='delete'),
    url(r'^ingrediente/create/$', CreateIngrediente.as_view(), name='create'),
    url(r'^ingrediente/list/$', ListIngrediente.as_view(), name='list'),
    url(r'^ingrediente/edit/(?P<id>[0-9]+)$', EditIngrediente.as_view(), name='edit'),
    url(r'^ingrediente/delete/(?P<id>[0-9]+)$', DeleteIngrediente.as_view(), name='delete'),
    url(r'^aula_ingrediente/create/$', CreateAulaIngrediente.as_view(), name='create'),
    url(r'^aula_ingrediente/list/$', ListAulaIngrediente.as_view(), name='list'),
    url(r'^aula_ingrediente/edit/(?P<id>[0-9]+)$', EditAulaIngrediente.as_view(), name='edit'),
    url(r'^aula_ingrediente/delete/(?P<id>[0-9]+)$', DeleteAulaIngrediente.as_view(), name='delete'),
     

]




'''urlpatterns = [
    url(r'^create/$', CreateAulaIngrediente.as_view(), name='create'),
    url(r'^list/$', ListAulaIngrediente.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditAulaIngrediente.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteAulaIngrediente.as_view(), name='delete'),

]'''

