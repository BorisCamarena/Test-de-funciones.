# Metodo de la secante.

# Importamos las librerias.

import matplotlib.pyplot as plt

import numpy as np

import sympy

# Utilizamos la funcion para graficar la funcion objetivo ya echa.

def GraficarFuncionObjetivo( ) :

  # Damos valores a las variables.

    a , b = 40 , 90
    
    T = np.linspace( a , b , 100 )

    # Ecuacion original.

    U = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    # Graficamos.

    plt.figure( figsize = ( 6 , 3 ) )

    plt.plot( T , U, 'b' )

    # Valores esperados.

    plt.plot( 55.08 , 1225.17 , 'ko' )

    plt.annotate( r'$55.08, 1225.17$', ( 55.08 , 1225.17 ) , ( 50, 1250 ) )

    plt.xlabel( " Temperatura. " )

    plt.ylabel( " Costo. " )

    plt.grid( )

    plt.show( )
    
    return None

GraficarFuncionObjetivo()



# De igual forma utilizamos la funcion calcularGradiente ya creada.

def CalcularGradiente( ) :

  # T como variable simbolica.

    T = sympy.Symbol( ' T ' )

    # Ecuacion original.

    fU = ( 204165.5 ) / ( 330 - 2 * T ) + ( 10400 ) / ( T - 20 )

    # Calculamos las derivadas.

    d1fU = sympy.diff( fU ) 

    # Mandamos a terminal.

    print( fU )

    print( d1fU )

    return None 

# LLamamos a la funcion.

CalcularGradiente( )

# Funcion objetivo.

def U( T ) :

    return 10400 / ( T - 20) + 204165.5 / ( 330 - 2 * T )


# Evaluamos.

U( 55.08 )

# Primera derivada.

def d1U( T ) :

    return - 10400 / ( T - 20) ** 2 + 408331.0 / ( - 2 * T + 330)** 2

# Evaluamos en la derivada.

d1U( 55.08 )


# Algoritmo de la secante.

# Asignamos valores y creamos la funcion del metodo.

def Secante( ) :

  # Definimos vaaribales, contador y registro como lista.

    a , b = 40 , 90

    epsilon = 0.01
    
    cont = 0

    registro = [ ]
    
    while True:

        # calcular f'( a ), ya que la utilizamos.

        dU_a = d1U( a )
        
        # calcular f'( b ), la usamos.

        dU_b= d1U( b )
        
        # calcular alpha. ( Analogo al codigo ya echo. )

        # Ecuacion de alpha.

        alpha = b - dU_b / ( ( dU_b - dU_a ) / ( b - a ) )

        dU_alpha = d1U( alpha )
        
        # Condicionante ya hecha.

        if dU_alpha > 0 :

            b = alpha

        else :

            a = alpha
            
        U_alpha = U( alpha )
        
        cont = cont + 1

        # Añadimos informacion al registro ya creado como una lista vacia.
        
        registro.append( [ cont , alpha , U_alpha ] )

        print( " It: {: 02d} - Temp: {: .10f} - Costo: {: .10f}".format( cont , alpha , U_alpha ) )

        # Condicion cercana a epsilon.
        
        if np.abs( dU_alpha ) <= epsilon :

            print( "------------------------------------------------------------------------" )

            print( " It: {: 02d} - Temp: {: .10f} - Costo: {: .10f}".format( cont , alpha, U_alpha ) )

            break
            
    return registro

# Finalizamos y mandamos a llamar a la funcion.

reg = Secante()

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
