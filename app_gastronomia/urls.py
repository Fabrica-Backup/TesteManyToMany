from django.conf.urls import url, include
from django.contrib import admin

#from aula.views import CreateAula
#from aula.views import CreateIngrediente, ListIngrediente, EditIngrediente, DeleteIngrediente
#from aula.views import CreateAulaIngrediente, ListAulaIngrediente, EditAulaIngrediente, DeleteAulaIngrediente

urlpatterns = [

    url(r'^api/', include('aula.urls')),
    

    #url(r'^api/aula/create/$', CreateAula.as_view(), name='create'),
    #url(r'^api/aula/list/$', ListAula.as_view(), name='list'),
    #url(r'^api/aula/edit/(?P<id>[0-9]+)$', EditAula.as_view(), name='edit'),
    #url(r'^api/aula/delete/(?P<id>[0-9]+)$', DeleteAula.as_view(), name='delete'),
    #url(r'^api/ingrediente/create/$', CreateIngrediente.as_view(), name='create'),
    #url(r'^api/ingrediente/list/$', ListIngrediente.as_view(), name='list'),
    #url(r'^api/ingrediente/edit/(?P<id>[0-9]+)$', EditIngrediente.as_view(), name='edit'),
    #url(r'^api/ingrediente/delete/(?P<id>[0-9]+)$', DeleteIngrediente.as_view(), name='delete'),
    #url(r'^api/aula_ingrediente/create/$', CreateAulaIngrediente.as_view(), name='create'),
    #url(r'^api/aula_ingrediente/list/$', ListAulaIngrediente.as_view(), name='list'),
    #url(r'^api/aula_ingrediente/edit/(?P<id>[0-9]+)$', EditAulaIngrediente.as_view(), name='edit'),
    #url(r'^api/aula_ingrediente/delete/(?P<id>[0-9]+)$', DeleteAulaIngrediente.as_view(), name='delete'),

]

'''urlpatterns = [
    url(r'^api/ingrediente/create/$', CreateIngrediente.as_view(), name='create'),
    url(r'^api/ingrediente/list/$', ListIngrediente.as_view(), name='list'),
    url(r'^api/ingrediente/edit/(?P<id>[0-9]+)$', EditIngrediente.as_view(), name='edit'),
    url(r'^api/ingrediente/delete/(?P<id>[0-9]+)$', DeleteIngrediente.as_view(), name='delete'),

]'''


'''urlpatterns = [
    url(r'^api/aula_ingrediente/create/$', CreateAulaIngrediente.as_view(), name='create'),
    url(r'^api/aula_ingrediente/list/$', ListAulaIngrediente.as_view(), name='list'),
    url(r'^api/aula_ingrediente/edit/(?P<id>[0-9]+)$', EditAulaIngrediente.as_view(), name='edit'),
    url(r'^api/aula_ingrediente/delete/(?P<id>[0-9]+)$', DeleteAulaIngrediente.as_view(), name='delete'),

]'''