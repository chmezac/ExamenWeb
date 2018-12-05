from django.shortcuts import render
from .models import Tienda, Producto
from rest_framework import viewsets
from .serializers import TiendaSerializer, ProductoSerializer

# Create your views here.
class TiendaViewSet( viewsets.ModelViewSet ):
    queryset = Tienda.objects.all().order_by( 'id' )
    serializer_class = TiendaSerializer

class ProductosViewSet( viewsets.ModelViewSet ):
    queryset = Producto.objects.all().order_by( 'id' )
    serializer_class = ProductoSerializer
