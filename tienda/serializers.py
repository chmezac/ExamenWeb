from .models import Tienda, Producto
from rest_framework import serializers

class TiendaSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = Tienda
        fields = ( 'id', 'nombre', 'direccion', 'ciudad', 'comuna', 'telefono', 'email')


class ProductoSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
            model = Producto
            fields = ( 'id', 'nombre', 'descripcion', 'precio', 'tipo')
