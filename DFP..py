# Metodo - DFP.

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

# Vista en clase.


def funcion( x ) :

    return 100 * ( x[ 1 ] - x[ 0 ]**2 )**2 + ( 1 - x[ 0 ] )**2

Dif = grad( funcion )

# Empezamos a definir el ploteo, con sus parametros.

# Para implementar el algoritmo con la funcion DFP.

x1 = np.linspace( - 10 , 10 , 100 )

x2 = np.linspace( - 10 , 10 , 100 )

I = np.zeros( ( [ len( x1 ) , len( x2 ) ] ) )

for i in range( 0 , len( x1 ) ) :

    for j in range( 0 ,  len( x2 ) ) :

        I[ j , i] = funcion( [ x1[ i ] , x2[ j ] ] )

# Empezamos el ploteo.

c = plt.contour( x1 , x2 , I , 100 , cmap = plt.cm.gnuplot )

plt.clabel( c , inline = 1 , fontsize = 10 )


plt.xlabel( " $ Eje --- x_1 $ ----> " )

plt.ylabel( " $ Eje --- x_2 $ ----> " )

# Definimos la funcion del algoritmo.

# Con su respectivo metodo.


def DFP( Tj , tol , ep1 , ep2 ) :

    x1 = [ Tj[ 0 ] ]

    x2 = [ Tj[ 1 ] ]

    P = np.eye( len( Tj ) )

    norma = np.linalg.norm

# Declaramos una variable global, para evadir el error de K, que dice 

# Que el valor de K se le habia asignado un valor previo.

# La declaramos como variable global.

    letter = " K "


    while True :

        Grad = Dif( Tj )

        # Definimos la direccion de descenso.

        d = - P.dot( Grad )

        # Dafinimos nuestro punto inicial x0.

        x0 = Tj 

        # Utilizamos la libreria from scipy.optimize import line_search para optimizar el programa.

        # Para seleccionar el tamaño de paso.

        Par = line_search( f = funcion , myfprime = Dif , xk = x0 , pk = d , c1 = ep1, c2 = ep2)[ 0 ] 

        if Par != None :

            K = Tj +  Par * d

        if norma( Dif( K ) )  < tol :

            x1 += [ K[ 0 ] , ]

            x2 += [ K[ 1 ] , ]

            # Ploteamos.

            plt.plot( x1 , x2 , "rx-" , ms = 5.5 ) 

            plt.show( )

            # Retornamos los varoles obtenidos.

            return K , funcion( K )

        else :

            Dj = K - Tj 

            # Utilizamos la funcion gradiente.

            Gj = Dif( K ) - Grad 

            p1 = Dj 

            p2 = P.dot( Gj ) 

            # Hacemos asignacion de variables.

            # Haciendo uso de la funcion gradiente.

            p1T = p1.T

            p2T = p2.T

            l1 = 1 / ( p1T.dot( Gj ) ) 

            l2 = - 1 / ( p2T.dot( Gj ) )

            p1 = np.outer( p1 , p1 )

            p2 = np.outer( p2 , p2 ) 

            d1 = l1 * p1 + l2 * p2 

            P += d1

            # Actualizamos los datos mediante iteraciones.

            Tj = K

            x1 += [ Tj[ 0 ] , ]

            x2 += [ Tj[ 1 ] , ]


            # Por ultimo, mandamos a llamar a la funcion, metiendo 

            # parametros previamente creados.

DFP( np.array( [ - 5.40 , - 4.25 ] ) , 10**-2 , 10**-7 , 5.40 )



