# Algoritmo dd busqueda exacta.

#Importamos las librerias.

import numpy as np

import math

import matplotlib.pyplot as plt

from numpy import *

import sys

import sympy as sy

# Podemos implementar los metodos y algoritmos vistos.

# Implementamos la funcion del metodo.

# Con sus restricciones.

# Definimos la funcion de busqueda exacta.

def Busqueda_exacta( f , x , alpha , p ) :

  # Implementamos las condiciones.

  condicion = np.dot( f( x + alpha * p ) , p ) == 0

  return condicion

# Implementamos el metodo con la funcion debusqueda exacta.

def Metodo( f , g , H , xk ) :

    # Definimos las variables.

  max = 100

  ro = 0.5

  sigma = 0.1

  k = 0

  # Definimos el parametro de error epsilon.

  epsilon = 1e-5

  while k < max :

    gk = g( xk )

    Hk = H( xk )

    dk = -1.0 * np.linalg.solve( Hk , gk )

    if np.linalg.norm( dk ) <  epsilon :

      break

    m = 0

    mk = 0

    while m < 20:

        if  Busqueda_exacta( g , xk , ro**m , dk ) :

            mk = m

            break

        m += 1

    xk += ro ** mk * dk

    k += 1

  print( " Resultado del Metodo. " )

  print( " El punto xk = " , xk )

  print( " La funcion evaluada f( xk ) = " , round(f( xk ) , 3 ) )

  print( " Numero de iteraciones es : " , k )


# Testeo.

f_counter = 0

g_counter = 0

H_counter = 0

x = sy.IndexedBase( ' x ' )

# Definimos cuantas variables habra en la funcion a optimizar.

n = 2

# Funcion vista en clase.


# Función de Rosenbrock.

fexpr = 100 * ( x[ 0 ]**2 - x[ 1 ] )**2 + ( x[ 0 ] - 1 )**2

gexpr = [ sy.diff( fexpr ,x[ i ] ) for i in range( n ) ]

Hexpr = [ [ sy.diff( g ,x[ i ] ) for i in range( n ) for g in gexpr ] ]

flambdify = sy.lambdify( x , fexpr , " numpy " )

glambdify =[ sy.lambdify( x , gf , " numpy " ) for gf in gexpr ]

Hlambdify = [ [ sy.lambdify( x , gf," numpy " ) for gf in Hs ] for Hs in Hexpr ]


# Definimos las siguientes funciones.


def funcion( x ) :

  global f_counter

  f_counter += 1

  return flambdify( x )

def gfuncion( y ) :

  global g_counter

  g_counter += 1

  return np.array( [ gf( y ) for gf in glambdify ] )

def Hessiano( y ) :

  global H_counter

  H_counter += 1

  return np.array( [ [ gf( y ) for gf in Hs ] for Hs in Hlambdify ] )

# Ejecutamos la funcion principal, que nos da las soluciones buscadas.

Metodo( funcion , gfuncion , Hessiano , np.zeros( n ) )
