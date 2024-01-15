# Metodo de Newton - Estacionario.

# La diferencia al metodo de Newton es que sustituimos A_k por H.

# Empezamos importando las librerias que necesitaremos.

import numpy as np

from math import sqrt 

# Comenzamos definiendo las funciones que necesitaremos.

# Hacemos uso de una funcion.

# Que nos ayudara a calcular la matriz H.

def funciones( x1 , x2 , x3 ) :

  # Coloque las funciones que desea evaluar.

  f1 = # Ingrese su funcion 1.

  f2 = # Ingrese su funcion 2.

  f3 = # Ingrese su funcion 3.

  # Si la funcion sera geometrica, con exponenciales.

  # Debe importarlas en la linea de codigo :

  # from math import sqrt , ... 

 # Imprimimos como una matriz en terminal. 

  return np.matrix( [ [ f1 ] , [ f2 ] , [ f3 ] ] ) 

# A continuacion creamos la funcion evaluar con sus derivadas parciales.

# Para calcular la matriz H.

def Evaluar( x1 , x2 , x3 ) : 

  # En la siguiente linea de codigo debe ingresar las derivadas parciales, separadas por columnas.

  # Ya que estamos haciendo uso de matrix de numpy.

  Eval = np.matrix( )

  Eval_diff = np.linalg.inv( Eval )

  # Nos regresa la matriz H.

  return [ Eval , Eval_diff ] 

# Elegimos un punto a evaluar.

# Puede modificarlo.

x0 = [ 1 ,  1  , 1 ]

# Damos valor a las variables.

r1 = 0 

# Definimos el punto..

x1 , x2 , x3 = x0

# Definimos la tolerancia o restriccion.

epsilon = 0.001

# Se le muestra la tabla de valores de solicitada.

# Haciendo uso del siguiente formato.

print( " -------------------------------------------------")

print( " r1 \t x1 \t x2 \t x3 \t || x( k ) - x( k - 1 ) ||   ")

print( " {0:1d} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f} \t  ".format( r1 , x1 , x2 , x3 ) )

print( " -------------------------------------------------")


# Declaramos las condiciones.

# Defina el n, para el cual se cumple la restriccion k menor que n.

while k < n : # Defina el n que quiere utilizar.

  Eval , Eval_diff = Evaluar( x1 , x2 , x3 )

  fun = funciones( x1 , x2 , x3 )

  R = - Eval_diff * fun

  # Hacemos el cambio.

  # La diferencia entre el método de Newton y Newton estacionario es que sustituimos 

  # A_k por el Hessiano.

  X = np.matrix( Eval_diff ).T + R

  # Obtenemos los valores la matriz con float.

  x1 , x2 , x3 = float( X[ 0 ][ 0 ] ) , float( X[ 1 ][ 0 ] ) , float( X[ 2 ][ 0 ] )

  # Calculamos el error.

  error = sqrt( ( x1 - x0[ 0 ] ) **2 + ( x2 - x0[ 2 ] ) **2 + ( x3 - x0[ 3 ] ) **2 )

  # Definimos nuevamente nuestro punto inicial.

  x0 = [ x1 , x2 , x3 ]

  r1 += 1

  # Se le muestra la tabla de valores de solicitada.

  # Haciendo uso del siguiente formato.

  print( " -------------------------------------------------")

  print( " r1 \t x1 \t x2 \t x3 \t || x( k ) - x( k - 1 ) || \t error \t  ")

  print( " {0:1d} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f} \t  {4:1.4f}  ".format( k , x1 , x2 , x3 , error ) )

  print( " -------------------------------------------------")







