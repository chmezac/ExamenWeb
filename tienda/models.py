from django.db import models

# Create your models here.

class Tienda( models.Model ):
    id = models.AutoField( primary_key = True )
    nombre_tienda = models.CharField( max_length = 100, blank = False, null = False )
    direccion = models.CharField( max_length = 100, blank = False, null = False )
    ciudad = models.CharField( max_length = 50, blank = False, null = False )
    comuna = models.CharField( max_length = 50 )
    telefono = models.CharField( max_length = 9 )
    email =  models.EmailField( max_length = 50 )
    encarg_tienda = models.CharField( max_length = 255)

    def __str__( self ):
        return self.nombre_tienda



class Producto( models.Model ):

    NOTEBOOKS = 'Notebooks'
    TARJETA_GRAFICA = 'Tarjeta_Grafica'
    AUDIFONOS = 'Audifonos'
    COMPUTADORES = 'Computadores'

    
    STATE_CHOICES = (
        (NOTEBOOKS, 'Notebooks'),
        (TARJETA_GRAFICA, 'Tarjeta_Grafica'),
        (AUDIFONOS, 'Audifonos'),
        (COMPUTADORES, 'Computadores'),
    )

    
    id = models.AutoField( primary_key = True )
    nombre_producto = models.CharField( max_length = 100, blank = False, null = False )
    descripcion = models.TextField( default= '' )
    precio = models.CharField( max_length = 10 )
    tipo = models.CharField( max_length=20, choices=STATE_CHOICES, default=NOTEBOOKS)
    imageUrl = models.CharField( max_length = 255, default = '' )

    def __str__( self ):
        return self.nombre_producto

    def __str__(self):
        return str(self.nombre_producto) + ": $" + str(self.precio)




class Vendedor( models.Model ):
    id = models.AutoField( primary_key = True )
    nombre_vendedor = models.CharField( max_length = 255 )
    
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length=30)


    def __str__( self ):
        return self.nombre_vendedor   


