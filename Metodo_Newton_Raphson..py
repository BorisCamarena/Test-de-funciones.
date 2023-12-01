# Importamos las librerias.

import matplotlib.pyplot as plt

import numpy as np

import sympy

# Creamos la funcion para graficar la funcion objetivo.

# Utilizamos la ecuacion del problema original.

def plotPuntos( a , b ) :

    T = np.linspace( a , b , 100 )

    U = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    return T, U

def GraficarFuncionObjetivo( ):

  # Limites de busqueda.

    a , b = 40 , 90

    # Obtener los valores con la funcion plotPuntos.

    T , U = plotPuntos( a , b )
    
    plt.plot( T , U , 'b' )

    # Por biseccion sabemos los valores.

    # Y ploteamos.

    plt.plot( 55.08 , 1225.17 , 'ko' )

    plt.annotate( r'$55.08 , 1225.17$' , ( 55.08 , 1225.17 ) , ( 50 , 1250 ) )

    plt.xlabel( ' Temperatura. ' )

    plt.ylabel( ' Costo. ' )

    plt.grid( )

    plt.show( )

GraficarFuncionObjetivo( )


# Calculamos el gradiente, con la siguente funcion.

def CalcularGradiente( ) :

  # Hacemos que T sea una variable simbolica.

    T = sympy.Symbol( ' T ' )

    # Ecuacion original.

    U = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    # Calculamos la primera derivada y segunda derivada de U.

    # Con la libreria sympy. 
    
    d1U = sympy.diff( U )

    d2U = sympy.diff( d1U )

    # Mandamos a terminal.
    
    print( U )
    print( d1U )
    print( d2U )

    # Mandamos a llamar la funcion.

CalcularGradiente()

# Mandamos a llamar la funcion U en T.

def U( T ) :

    return 10400 / ( T  - 20 ) + 204165.5 / ( 330 - 2 * T )

# Evaluamos la funcion en 55.08.

U( 55.08 )

#  Verificamos la primera y segunda derivada.

def d1U( T ):

    return -10400 / ( T - 20 ) ** 2 + 408331.0 / ( 330 - 2 * T ) ** 2

d1U( 55.08 ) 

def d2U( T ) :

    return 20800 / ( T - 20 ) ** 3 + 1633324.0 / ( 330 - 2 * T ) ** 3

d2U( 55.08 )

# Evaluamos la primera y segunda derivada en 55.08 para 

# corroborar que esten correctas.

# Ahora podemos proceder ya que verificamos las derivadas, al metodo de 

# Newton - Raphson.

# Definimos la funcion objetivo.

def NewtonRaphson( ) :

  # Definimos los valores de las variables, segun el metodo.

    a , b = 40 , 90

    x = 90

    epsilon = 0.001

    # Cremos la variables contador y un registro, como lista vacia.

    cont = 0

    registro = [ ]
    
    while True:

        # Calculo de f'(x) y f''(x)

        d1U_x = d1U( x )

        d2U_x = d2U( x )

        # Asignamos el valor previo de x.

        # Siguendo el metodo.
        
        xprev = x

        x = xprev - d1U_x / d2U_x

        # Llamamos a la funcion.
        
        U_x = U( x )
        
        cont = cont + 1

        # Agregamos informacion a la lista.

        registro.append( [ cont , x , U_x ] )
        
        print( " It : {:02d} - Temp: {: .10f} - Costo: {: .10f}".format( cont , x , U_x ) )
        
        # Creamos una condicion que determine el valor absoluto de x y x previa.

        # Cuando este cerca del valor epsilon.

        if( np.abs( x - xprev ) <= epsilon ) :

            print( " ---------------------------------------------------------------- " )

            
            # Hacemos el registro.

            print( " It: {: 02d} - Temp: {: .10f} - Costo: {: .10f} ".format( cont , x , U_x ) )

            break
        
    return registro

# Mandamos a llamar al la funcion del metodo.

reg = NewtonRaphson( )

# Creamos la funcion de evaluar registro.

# Copiamos el codigo del metodo de la biseccion.

# Para plotear, caracteriza, graficar y darle color a las graficas.

def evaluacion( reg ) :

  # Utilizamos np.array para matrices.

    reg = np.array( reg )

    fig , axs = plt.subplots( 1 , 2 , figsize = ( 15 , 6 ) )
    
    fig.suptitle( ' Analisis de convergencia. ' )
    
    axs[ 0 ].axhline( 55.08, color ='k' , linewidth = 3 , linestyle = '--' )

    axs[ 0 ].plot( reg[ : , 0 ] , reg[ : , 1 ] , linewidth = 4 )

    axs[ 0 ].set_xlabel( ' Iteraciones. ' )

    axs[ 0 ].set_ylabel( 'Temperatura.' ) 

    axs[ 0 ].grid( )

    axs[ 0 ].set_xlim( [ 0 , 15 ] )
    
    axs[ 1 ].axhline( 1225.17 , color = 'k', linewidth = 3 , linestyle = '--' )

    axs[1].plot( reg[ : , 0 ] , reg[ : , 2 ] , linewidth = 4 )

    axs[ 1 ].set_xlabel( ' Iteraciones. ' )

    axs[ 1 ].set_ylabel( ' Costo. ' )

    axs[ 1 ].grid( )

    axs[ 1 ].set_xlim( [ 0 , 15 ] )
    
    plt.show( )

evaluacion( reg )
 
