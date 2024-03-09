from django.urls import path
from . import views,htmx_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("loja/", views.loja, name="loja"),
    path("contact/", views.contact, name='contact'),
    path("formulario/", views.formulario, name='formulario'),
    path("categoria/<str:nome>", views.categorias, name='categoria'),
    path("produto/<int:id>", views.produto, name='produto'),
    path("add_carrinho", views.add_carrinho, name='add_carrinho'),
    path("ver_carrinho", views.ver_carrinho, name='ver_carrinho'),
    path("remover_carrinho/<int:id>", views.remover_carrinho, name='remover_carrinho'),
]

htmx_patterns =[
    path('search/',htmx_views.search, name='search')
]

#urlpatterns += htmx_patterns
