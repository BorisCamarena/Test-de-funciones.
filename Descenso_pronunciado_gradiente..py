# Desenso pronunciado del gradiente.

# Implementamos librerias que nos ayuden a hacer el codigo mas optimo.

# utilizando scipy.optimize import line_search podemos optimizarlo en gran medida.

# Que fue vista en clase.

# Utilizando otras librerias para plotear y numpy.

import numpy as np

# Librerias que nos ayudaran con el gradiente.

import autograd.numpy as au

from autograd import grad

# Plotear.

import matplotlib.pyplot as plt

# Libreria vista en clase para la busqueda lineal.

from scipy.optimize import line_search


# Definimos la funcion de Rosenbrock.


def funcion( x ) :

    return 100 * ( x[ 1 ] - x[ 0 ]**2 )**2 + ( 1 - x[ 0 ] )**2

Dif = grad( funcion )

norma = np.linalg.norm


# Importante :

# Elija los parametros para x1 y x2.


x1 = np.linspace( - 3 , 3 , 100 )

x2 = np.linspace( - 3 , 3 , 100 )

z = np.zeros( ( [ len( x1 ) , len( x2 ) ] ) )

for i in range( 0 , len( x1 ) ) :

    for j in range( 0 , len( x2 ) ) :

        z[ j , i ] = funcion( [ x1[ i ] , x2[ j ] ] )


# Empezamos el proceso de ploteo en terminal.


c = plt.contour( x1 , x2 , z , 100 , cmap = plt.cm.gnuplot )

plt.clabel( c , inline = 1 , fontsize = 10 ) 

plt.xlabel( " $ x_1 $  -> " )

plt.ylabel( " $ x_2 $  -> " )


# Definimos la funcion de descenso pronunciado.

# Como en la teoria vimos que se deben elegir los parametros para la condicion de paro.

# sus epsilon's.

# Asi en la definicion de la funcion se eligen para que al llamarla al final del codigo 

# pueda elegir sus parametros.


def Direccion_Pronunciada( Xj , tol_1 , tol_2 , tol_3 , epsilon1 , epsilon2 ) :

    x1 = [ Xj[ 0 ] ]

    x2 = [ Xj[ 1 ] ]

    while True :

        D = Dif( Xj ) 

        # Direccion pronunciada de descenso.

        # Seleccionamos la direccion de descenso.

        par = - D / norma( D )

        # Elegimos nuestro punto inicia x0 o xk.
        
        x0 = Xj  

        ep = line_search( f = funcion , myfprime = Df, xk = x0, pk = par , c1 = epsilon1, c2 = epsilon2 )[ 0 ] 

        if ep != None :

            X = Xj + ep * par

            # Implementamos el algoritmo con sus parametros y condiciones de paro.

            # Para el nuevo descenso.

            # Condiciones de paro vistas en clase.

            # Tomamos como tol_3 a epsilon3.

        if norma( X - Xj ) < tol_1 and norma( Dif( X ) ) < tol_2 or abs( funcion(X) - funcion( Xj ) ) < tol_3 :

            x1 += [ X[ 0 ] , ]

            x2 += [ X[ 1 ] , ]

            # Ploteamos la direccion que llevamos.

            plt.plot( x1 , x2 , "rx-" , ms = 5.5 )

            plt.show( )

            # Nos retorna el optimo x*.

            return X , funcion( X )

            # Si no ...

            # Hacemos el asignamiento de x a Xj.

        else :

            Xj = X

            x1 += [ Xj[ 0 ] , ]

            x2 += [ Xj[ 1 ] , ]


print( " ------------------------------------------------------------ " )

print( " ----- Funcion de Rosenbrock - direcciones a ( 1 , 1 ). ----- " )

print( " ------------------------------------------------------------ " )


# Elija sus parametros.


Direccion_Pronunciada( np.array( [ 1.1 , 2.2 ] ) , 10**-4 ,  10**-3 , 10**-5 , 10**-5 , 0.212 )




