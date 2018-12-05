from django.db import models

# Create your models here.

class Tienda( models.Model ):
    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 100, blank = False, null = False )
    direccion = models.CharField( max_length = 100, blank = False, null = False )
    ciudad = models.CharField( max_length = 50, blank = False, null = False )
    comuna = models.CharField( max_length = 50 )
    telefono = models.CharField( max_length = 9 )
    email =  models.EmailField( max_length = 50 )
    #falta encargado de la tienda

    def __str__( self ):
        return self.nombre



    

class Producto( models.Model ):

    PRODUCTO1 = 'Producto 1'
    PRODUCTO2 = 'Producto 2'
    PRODUCTO3 = 'Producto 3'
    
    STATE_CHOICES = (
        (PRODUCTO1, 'Producto 1'),
        (PRODUCTO2, 'Producto 2'),
        (PRODUCTO3, 'Producto 3'),
    )

    
    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 100, blank = False, null = False )
    descripcion = models.TextField( default= '' )
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    tipo = models.CharField( max_length=10, choices=STATE_CHOICES, default=PRODUCTO1)
    

    def __str__( self ):
        return self.nombre

    def __str__(self):
        return str(self.nombre) + ": $" + str(self.precio)


