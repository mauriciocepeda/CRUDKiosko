from django.urls import path
from .views import inicio, BuscarProducto, EliminarProducto, NuevoProducto, CrearProducto, EdicionProducto, EditarProducto
urlpatterns = [
    path('',inicio,name='inicio'),
    path('EliminarProducto/<marca>/<categoria>', EliminarProducto, name='EliminarProducto'),
    path('NuevoProducto/', NuevoProducto, name='nuevoprodu'), #renderiza la pagina
    path('CrearProducto/', CrearProducto, name='CrearProducto'), #envia el form
    path('EdicionProducto/<marca>/<categoria>', EdicionProducto, name='EdicionProducto'), #renderiza la pagina
    path('EditarProducto/', EditarProducto, name='EditarProducto'), #envia el form
    path('BuscarProducto/', BuscarProducto, name='BuscarProducto'),
    path('BuscarProducto/EliminarProducto/<marca>/<categoria>', EliminarProducto),
    path('BuscarProducto/EdicionProducto/<marca>/<categoria>', EdicionProducto),
]