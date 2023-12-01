# Importamos las librerias.

print("Gradiente.")

import sympy

# Definimos la funcion con sus variables.

def calcularGradiente():

  T = sympy.Symbol('T')

  fu = (204165.5)/(330-2*T) * (10400)/(T-20)

  # Calculamos la derivada con la funcion diff( )

  d1fu = sympy.diff(fu)

  print("Funcion y su derivada:")

  print(fu)

  print(d1fu)

  return None 

calcularGradiente( )

# Hacemos otra funcion evaluada en T.

def U( T ):

   return (10400)/(T-20) * (204165.5)/(-2*T+ 300) 

U(55.08)

# Primera derivada de U.

def dU(T):

  # Derivada evaluada en el punto T.

  return -10400/(T-20)**2 + 408331.0/(-2*T + 330 )**2

dU(55.08)
