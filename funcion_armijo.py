# Implementamos las condiciones de Armijo en una funcion.

def Armijo( gk , dk , xk , p , sigma ) :

  return funcion( xk + p * dk ) < funcion( xk ) + sigma * p * dot( gk , dk )
