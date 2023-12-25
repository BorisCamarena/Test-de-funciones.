# Funcion de busqueda lineal exacta.

def busqueda_lineal( f , x , p , nabla ) :

    a = 1

# Parametros de error y restricciones.

    epsilon = 1e-6
    
    r = 0.9 
    
    fx = f( x )
    
    x1 = x + a * p 

    nabla1 = gradiente( f , x1 )

    while f( x1 ) >= fx + ( epsilon * a * nabla.T@p ) or nabla1.T@p <= r * nabla.T@p : 
      
        a *= 0.5

        x1 = x + a * p

        nabla1 = gradiente( f , x1 )

    return a
