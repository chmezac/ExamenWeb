from .models import Tienda, Producto, Vendedor
from rest_framework import serializers

class TiendaSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = Tienda
        fields = ( 'id', 'nombre_tienda', 'direccion', 'ciudad', 'comuna', 'telefono', 'email', 'encarg_tienda')


class ProductoSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
            model = Producto
            fields = ( 'id', 'nombre_producto', 'descripcion', 'precio', 'tipo', 'imageUrl')


class VendedorSerializer ( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Vendedor
        fields = ( 'id', 'nombre_vendedor', 'email', 'password')
