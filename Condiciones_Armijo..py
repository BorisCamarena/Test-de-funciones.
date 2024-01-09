# Programa de descenso de gradiente -  Armijo.

# Importamos las librerias que vamos a utilizar.

import numpy as np

import sympy as sp

# Para utilizar una funcion de dos variables, tenemos que declarar a 

# x como variable simbolica y 

# y como variable simbolica.

x = sp.symbols( ' x ' )

y = sp.symbols( ' y ' )

# Ya con esto podemos crear nuestra funcion a probar.

# Puede considerar una funcion e implementarla, en este caso para probar el metodo, utilice x**2.

funcion = x **2

# Creamos el gradiente de la funcion.

# Haciendo uso de diff para las derivadas parciales.

# Es muy parecido a matlab.

# Haciendo uso del for i in ( x , y )

# Vamos recorriendo la funcion y aplicando derivadas para obtener el gradiente.

funcion_gradiente = [ sp.diff( f , i ) for i in ( x , y ) ]

iteraciones = 100

# Como parte del metodo, tenemos que evaluar el gradiente en el punto inicial elegido.

def Evaluacion( xk ) :

    return np.array( [ grad.subs( { x : x0[ 0 ]  , y : x0[ 1 ] } ).evalf( ) for grad in funcion_gradiente ] , dtype = float )


# Implementamos la funcion Armijo, con sus condiciones.


def Armijo( x0 , ep = 1 , l = 0.5 , alpha = 0.5 , condicion_paro =  1e-5 , iteraciones = 100 ) :


  # Se utilizan comandos usados en los otros programas.

    iteraciones = 100  

    xk  = np.array( x0 , dtype = float )

    for _ in range( iteraciones ) :

        grad = Evaluacion( xk )

        if np.linalg.norm( grad ) < condicion_paro :

            break

        while True :

            x_asterisco = xk - ep * grad

            if f.subs( { x: x_asterisco[ 0 ] , y: x_asterisco[ 1 ] } ) <= funcion.subs( { x: xk[ 0 ] , y : xk[ 1 ] } ) + l * ep * np.dot( grad , - grad ) :

                break

            ep *= alpha

        xk = x_asterisco

    return xk

# Elegimos el punto inicial donde queremos empezar la evaluacion.

x0 = [ 3 , 4 ]

x_optimo = Armijo( x0 )


print( "----------------------------------------------------- " )

print( "Resultados:")

print( " Su función es : " ,  funcion )

print( " El gradiente de su funcion es : " , funcion_gradiente )

# print( " La norma de su gradiente es : " ,  N )

print( " Su punto óptimo encontrado ( x0 ) es : " , x_optimo )

print( " Número de Iteraciones : " , iteraciones )

print( "----------------------------------------------------- " )
