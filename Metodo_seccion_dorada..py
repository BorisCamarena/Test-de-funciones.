# Metodo de la seccion dorada.

import matplotlib.pyplot as plt

import numpy as np

# Las siguientes funciones ya fueron creadas en los metodos anteriores, por lo que se asume ya esta entendido.

def plotPuntos( a , b ) :

    T = np.linspace( a , b , 100 )

    U = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    return T, U

def GraficarFuncionObjetivo( ) :

    a , b = 40 , 90
    
    T = np.linspace( a , b, 100 )

    U = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    plt.figure( figsize = ( 6 , 3 ) )

    plt.plot( T , U, 'b' )

    plt.plot( 55.08 , 1225.17 , 'ko' )

    plt.annotate( r'$55.08, 1225.17$', ( 55.08 , 1225.17 ) , ( 50 , 1250 ) )

    plt.xlabel( " Temperatura. " )

    plt.ylabel( " Costo. " )

    plt.grid( )

    plt.show( )
    
GraficarFuncionObjetivo( )

# Funcion objetivo.

def U( T ) :

    return ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

U( 55.08 )

# Metodo de la seccion dorada.

def GoldenSectionSearch( ) :

  # Definimos variables y le asignamo valores.

    a = 40

    b = 90

    # Asignamos parametros.

    tau = 2 - 1.618033988

    epsilon = 1e-6

    # Contador y lista vacia.

    cont = 0

    registro = [ ]

    while( True ) :

      # Seguimos el metodo.

        # Calcular alpha1 y alpha2.

        alpha1 = a * ( 1 - tau ) + b * tau

        alpha2 = a * tau + b *( 1 - tau ) 

        # Calcular f(alpha1) y f(alpha2).

        U_alpha1 = U( alpha1 )

        U_alpha2 = U( alpha2 )

        # Planteamos la siguiente condicion del metodo y paro.
        
        if( U_alpha1 > U_alpha2 ) :

            a = alpha1

        else :

            b = alpha2       

        cont = cont + 1

        registro.append( [ cont , alpha1 , U_alpha1 ] )

        print("It: {:02d} - Temp: {:.10f} - Costo: {:.10f}".format( cont, alpha1, U_alpha1 ) )

        # Planteamos la siguiente condicion para el registro.

        if( np.abs( U_alpha1 - U_alpha2 ) < epsilon ) :

            print( " ------------------------------------------------------- " )

            print( " It : {: 02d} - Temp: {: .10f} - Costo: {: .10f}".format( cont , alpha1 , U_alpha1 ) )

            break
            
    return registro

#  Mandamos a llamar a la funcion.

reg = GoldenSectionSearch( )

# Funcion de evaluacion ya echa.

# Analisis de convergencia.

def Evaluacion( reg ) :

    # Numpy array para matrices-

    reg1 = np.array( reg ) 

    fig , axs = plt.subplots( 1 , 2 , figsize = ( 15 , 4 ) )

    fig.suptitle( ' Convergencia. ' )

    axs[ 0 ].axhline( 55.08 , color = 'k' , linewidth = 3 , linestyle='--' )

    axs[ 0 ].plot( reg1[ : , 0 ], reg1[ : , 1 ] , linewidth = 4 )

    axs[ 0 ].set_xlabel( ' Iteraciones. ' )

    axs[ 0 ].set_ylabel( ' Temperatura. ' )

    axs[ 0 ].grid( )

    axs[ 0 ].set_xlim( [ 0 , 15 ] )

    axs[ 1 ].axhline( 1225.17 , color = 'k' , linewidth = 3 , linestyle = '--' )

    axs[ 1 ].plot( reg1[ : , 0 ] , reg1[ : ,2 ] , linewidth = 4 )

    axs[ 1 ].set_xlabel( ' Iteraciones. ' )

    axs[ 1 ].set_ylabel( ' Costo. ' )

    axs[ 1 ].grid( )

    axs[ 1 ].set_xlim( [ 0 , 15 ] )

    plt.show( )
    
    return None

Evaluacion( reg )

