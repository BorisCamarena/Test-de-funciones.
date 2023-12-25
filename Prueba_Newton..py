# Prueba para el metodo visto en clase con metodo de Newton.

# Algoritmo de Newton.

import sympy


# Insertamos la funcion.


def funcion(  ) :

  x = sympy.Symbol( ' x ' )

  fh = ( x**2 + ( 2 * x**2 ) + x**9 )

# Calculamos el gradiente.

  d1fh = sympy.diff( fh )

  print( " Su funcion es : " , fh )

  print( " Su Gradiente es : " , d1fh )

  return None

funcion( )

# Elija el punto xk.

def evaluar( x ) :

  # Misma funcion.

  fh = ( x**2 + ( 2 * x**2 ) + x**9 )

  return fh

  # Definimos la direccion d.

  d = -1

  # Gradiente cuadrado.

  cuadrado = ( fh ) ** 2



  print( " Su gradiente cuadrado es : " , cuadrado )

  print( " Su funcion h( x ) es : " , cuadrado * d + fh )

  print(" Su f( xk ) es : " , evaluar( 1 ) )

def Gradcua( x ) :

  cuadrado = ( x**9 + 3 * x**2 ) **2

  return cuadrado

R = Gradcua( 1 )
d = -1

print( " Su resultado del menos gradiente de la funcion evaluado en el punto xk es : " )

print( " -G( f( xk ) ) = " , R * d )

R = Gradcua( 1 )

# Implementamos el algoritmo, eligiendo el xk en la funcion anterior.

# Utiliza la direccion, propone un lambda, escoge el parametro epsilon.

def Algoritmo( ) :

  xk = 1

  d = -1

  lamb = 5

  epsilon = 1e-5

  x_k1 = xk + lamb * d

  if x_k1 < epsilon :

    print( " Su punto xk + 1 es : " , x_k1 )

  else :

   print( " Su punto xk + 1 es : " ,  x_k1 = xk + lamb * d )

Algoritmo( )
