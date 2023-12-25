
# Implementacion del metodo BFGS, con metodos vistos en clase.


# Importamos las librerias.

import numpy as np 

import matplotlib.pyplot as plt 

# Definimos la funcion a optimizar.

# Usando la funcion vista en clase.

def f( x ) :

    d = len( x )

    # Funcion vista en clase.

    return sum( 100 * ( x[ i + 1 ] - x[ i ]** 2 )**2 + ( x[ i ] - 1 )**2 for i in range( d - 1 ) )


# Funcion gradiente.


def gradiente( f , x ) : 

    h = np.cbrt( np.finfo( float ).eps )

    d = len( x )

    nabla = np.zeros( d )

    for i in range( d ) :

        x_p = np.copy( x ) 

        x_r = np.copy( x )

        x_p[ i ] += h 

        x_r[ i ] -= h

        nabla[ i ] = ( f( x_p ) - f( x_r ) ) / ( 2 * h )

    return nabla 


    # Funcion de busqueda lineal exacta.

def busqueda_lineal( f , x , p , nabla ) :

    a = 1

    # Parametros de error y restricciones.

    epsilon = 1e-4 
    
    r = 0.9 
    
    fx = f( x )
    
    x1 = x + a * p 

    nabla1 = gradiente( f , x1 )

    while f( x1 ) >= fx + ( epsilon * a * nabla.T@p ) or nabla1.T@p <= r * nabla.T@p : 
      
        a *= 0.5

        x1 = x + a * p

        nabla1 = gradiente( f , x1 )

    return a


# Implementacion del algoritmo.

# Con el metodo de Newton.


def BFGS( f , x0 , max_it , plot = False ) :

    d = len( x0 )

    nabla = gradiente( f , x0 )   

    # Hessiano.

    H = np.eye( d )

    x = x0[ : ]

    it = 2

# Ploteamos la grafica.

    if plot == True :

        if d == 2 :

            xl =  np.zeros( ( 1 , 2 ) ) 

            xl[ 0 , : ] = x 

        else :

            print( ' Sus dimensiones exceden. ' )

            plot = False

            # Norma del gradiente y vemos si es positivo.

            # Con sus parametros de error.

    while np.linalg.norm( nabla ) > 1e-5 :

        if it > max_it : 

            print( ' Numero de iteraciones. ' )

            break

            # Iteraciones.

        it += 1

        # Metodo de Newton con busqueda exacta.

        p = - H@nabla 

        a = busqueda_lineal( f , x , p , nabla )

        s = a * p

        x1 = x + a * p 

        nabla1 = gradiente( f , x1 )

        y = nabla1 - nabla

        y = np.array( [ y ] )

        s = np.array( [ s ] )

        y = np.reshape( y , ( d , 1 ) )

        s = np.reshape( s , ( d , 1 ) )

        r = 1 / ( y.T@s )

        li = ( np.eye( d ) - ( r * ( ( s@( y.T ) ) ) ) )

        ri = ( np.eye( d ) - ( r * ( ( y@( s.T ) ) ) ) )

        hess_inter = li@H@ri

        H = hess_inter + ( r * ( ( s@( s.T ) ) ) )

        nabla = nabla1[ : ]

        x = x1[ : ]

        # Ploteamos.

        if plot == True :

            xl = np.append( xl , [ x ] , axis = 0 )

    if plot == True : 

        x1 = np.linspace( min( xl[ : , 0 ] - 0.5 ) , max( xl[ : , 0 ] + 0.5 ) , 30 )

        x2 = np.linspace( min( xl[ : , 1 ] - 0.5 ) , max( xl[ : , 1 ] + 0.5 ) , 30 )

# Hacemos el proceso para crear la malla y plotear. Muy parecido a matlab.

        X1 , X2 = np.meshgrid( x1 , x2 )

        Z = f( [ X1 , X2 ] )

        plt.figure( )

        plt.title( ' Su punto óptimo se encuentra en  : ' + str( xl[ - 1 , : ] ) + ' \n # ' + str( len( xl ) ) + ' Iteraciones : ' )

        plt.contourf( X1 , X2 , Z , 30 , cmap = 'jet' )

        plt.colorbar( )

        plt.plot( xl[ : , 0 ] , xl[ : , 1 ] , c = 'w' )

        plt.xlabel( ' $ x_1 $ ' ) ; plt.ylabel( ' $x_2$ ' )

        plt.show( )

    return x

# Punto optimo.

# Poner el punto donde quiere iniciar la busqueda.

x_k_optimo = BFGS( f , [ -1.100 , 1 ] , 200 , plot = True )




