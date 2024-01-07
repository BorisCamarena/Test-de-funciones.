# Descenso de gradiente con busqueda exacta.

# Importamos las librerias que necesitamos.

from numpy import arange

# Con la biblioteca vista en clase nos ayudamos de line_search para optimizar el programa.

from scipy.optimize import line_search

# Biblioteca para plotear.

from matplotlib import pyplot

# Se define la funcion objetico en el return de a funcion.

# Tanto la funcion - funcion y la funcion - gradiente

# son de los metodos vistos en los ejercicios de tarea.


def funcion( x ) : 

	# Ejemplo:

	return 100 * x **2 - x

# Definimos el gradiente de la funcion objetivo.

def gradiente( x ) :

	return 200 * x - 1

# Definimos el x0.

x0 = - 1

# Definimos la direccion d - movimiento.

d = 10

# Empezamos a implementar el algoritmo con sus restricciones.

print('--------------------------------------------------------------------------------')

print(' Resultados :')

print( ' * x0 = %.1f , d = %.1f' % ( x0 , d ) )

# Utilizamos line_search de la libreria scipy.optimize.

x_k_optimo = line_search( funcion , gradiente , x0 , d )

# Definimos la variable ep.

ep = x_k_optimo[ 0 ]

print( ' * Ep : %.3f' % ep )

print( ' * Funcion evaluada en el punto óptimo - Iteraciones : %d' % x_k_optimo[ 1 ] )

# Implementamos la ecuacion iterativa del metodo vista en clase.

x_asterisco = x0 + ep * d

# Evaluamos x_asterisco en la funcion.

print( ' * f( x* ) = f( %.3f ) = %.3f' % ( x_asterisco , funcion( x_asterisco ) ) )

print('--------------------------------------------------------------------------------')

# Empezamos el proceso para plotear en terminal.

# Haremos un ploteo de x0 y x_asterico.

# Con x0 el punto inicial que propusimos.

# Y por ultimo como x_asteristo que es el punto optimo encontrado.

# Para eso empezamos a definir las variables para proceder a plotearlo.

# Definimos la escala de la grafica.

min , max = - 15.0 , 10.0

i = arange( min , max , 0.1 )

iter = [ funcion( x ) for x in i ]

pyplot.plot( i , iter , '-' , label = ' Funcion Objetivo.' )

# Ploteamos, eligiendo el estilo de la grafica y los puntos.

#  Funcion evaluada en el punto x0.

pyplot.plot( [ x0 ] , [ funcion( x0 ) ] , 's', color = 'r' )

# Funcion evaluada en el punto optimo.

pyplot.plot( [ x_asterisco ] , [ funcion( x_asterisco ) ] , 's', color = 'g' )

# Ploteamos en terminal.

pyplot.legend( )

pyplot.show( )
