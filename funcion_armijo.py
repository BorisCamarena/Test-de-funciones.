# Implementamos las condiciones de Armijo en una funcion.

def Armijo( gk , dk , xk , p , ep1 ) :

  return funcion( xk + p * dk ) < funcion( xk ) + ep1 * p * dot( gk , dk )
