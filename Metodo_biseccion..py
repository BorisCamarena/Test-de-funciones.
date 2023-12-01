# Metodo de la biseccion.

import numpy as np

print("Biseccion.")

print("Registro total - Temperatura - Costo.")

# Creamos la funcion biseccion.

def biseccion( ) :

  # Valor de las variables mas un epsilon-

    a = 40

    b = 90

    epsilon = 0.001


    # Inicializamos un contador.
    
    cont = 0

    registro = [ ]

    # Empezamos a implementar el algoritmo.
    
    while( True ) :

        alpha = ( a + b ) / 2
        
        # Primera derivada en a.

        dU_a = dU( a )
        
        # Primera derivada en alpha.

        dU_alpha = dU( alpha )

        # Condicion de paro.
        
        if( dU_a * dU_alpha < 0 ) :

            b = alpha

        else:

            a = alpha
            
        Ua = U( a )    
        
        # Condicion de finalizacion.

        # Usamos el valor absoluto.

        if( np.abs( a - b ) < epsilon ) :

          # Creamos un espacio.

            print('-------------------------------------------------------------')

            print(" It: {:02} - Temp: {:.10f} - Costo {:.10f}".format( cont , a , Ua ) )

            break
            
        cont = cont + 1

        registro.append( [ cont , a , Ua ] )

        # Implementamos con format para el contador y registro.

        print( "It: {:02} - Temp: {:.10f} - Costo {:.10f}".format( cont , a , Ua ) )
        
    return registro

        
reg1 = biseccion()

# Evolucion del metodo.

# Creamos su funcion.

def evaluacion( reg ) :

  # Utlizamos numpy array para matrices-

    reg = np.array( reg )

    fig , axs = plt.subplots( 1, 2, figsize = ( 15, 6 ) ) 
    
    fig.suptitle( ' Analisis de convergencia.' )

    # Ploteamos dando caracteristicas, variables y color.
    
    axs[ 0 ].axhline( 55.08 , color = 'k' , linewidth = 3 , linestyle = '--' )

    axs[ 0 ].plot( reg[ : , 0 ] , reg[ : , 1 ] , linewidth = 4 )

    axs[ 0 ].set_xlabel( ' Iteraciones. ' )

    axs[ 0 ].set_ylabel( ' Temperatura. ' )

    axs[ 0 ].grid( )

    axs[ 0 ].set_xlim( [ 0 , 15 ] )
    
    axs[ 1 ].axhline( 1225.17 , color = 'k', linewidth = 3 , linestyle = '--' )

    axs[ 1 ].plot( reg[ : , 0 ] , reg[ : , 2 ] , linewidth = 4 )

    axs[ 1 ].set_xlabel( ' Iteraciones. ' )

    axs[ 1 ].set_ylabel( ' Costo. ' )

    axs[ 1 ].grid( )

    axs[ 1 ].set_xlim( [ 0 , 15 ] )
    
    plt.show( )

    # Utilizamos el registro creado con la funsion biseccion.
    
# Obtenemos un registro total y completo, tanto numericamente, incluyendo la temperatura, costo, graficas.

# Numero de iteraciones y el analisis de convergencia.
    
# Mandamos a llamar a la funcion.

evaluacion( reg1 )
