
# Condiciones de Armijo - Wolfe.

# Optimizacion.

# Importamos las librerias que necesitamos.

import sympy as sympy

import numpy as np

import sympy as sp


# Declaramos las variables.

# Haciendo uno de numpy as np, useamos roll para trabajar las matrices.

valor = float ( roll[ 6 : 8 ] )

# Para utilizar una funcion de dos variables, tenemos que declarar a

# x como variable simbolica y

# y como variable simbolica.

x = sp.symbols( ' x ' )

y = sp.symbols( ' y ' )

# Ingresamos la funcion a evaluar.

# Puede modificar la funcion.

funcion = ( ( x - int( val ) ) **2 ) + ( ( y - ( 2 * x ) ) **2 ) 

f = sympy.sympify( funcion )

# Hacemos el gradiente de la funcion.

# Usando diff, que es muy parecido a matlab.

Dif = [ sympy.diff( funcion , x ) , sympy.diff( funcion , y ) ]

# Ingresamos las restricciones del algoritmo.

# Definimos las variables.

epsilon = np.array( 0.001 ).astype( np.float64 )

alpha_1 = 1.0  

ep = 0.5

beta_1 = 0.0001

beta_2 = 0.9

# Ingresamos el punto inicial x0.

x0 = [ valor + 3 , ( 2 * valor ) - 2 ]  

# Inicializamos el numero de iteraciones.

# Contador.

IT = 1  

# Imprimimos valores en la terminal.

print( " --------------------------------------------------")

print( " Valores de las variables del algoritmo. " )

print( ' roll : ' + str( roll ) )

print( ' val : ' + str( valor ) )

print( ' Su función : ' + str( funcion ) )

print( ' fx_eq : ' + str( f ) )

print( ' delfx_eq : ' + str( Dif ) )

print( ' epsilon : ' + str( epsilon ) )

print( ' alpha_1 : ' + str( alpha_1 ) )

print( ' ep : ' + str( ep ) )

print( ' beta_1 : ' + str( beta_1 ) )

print( ' beta_2 : ' + str( beta_2 ) )

print( ' Su punto inicial x0 es : ' + str( x0 ) )

print( ' Iteraciones : ' + str( IT ) )

print( " --------------------------------------------------")


# Hacemos la funcion para evaluar la funcion.

def Evaluar( val_x ) :

  # En x,y.

    fx = f.subs( [ ( x , val_x[ 0 ] ) , ( y , val_x[ 1 ] ) ] )

  # Devolvemos el valor en decimal o flotante.

    return np.array( fx ).astype( np.float64 )

# Obtener los valores de la funcion evaluada.

def Obtener_evaluacion( val_x ) :

  # En x,y.

    val1 = [ Dif[ 0 ].subs( [ ( x,  val_x[ 0 ] ) , ( y , val_x[ 1 ] ) ]  ) , Dif[ 1 ].subs( [
        ( x , val_x[ 0 ] ) , ( y , val_x[ 1 ] ) ] ) ]

  # Devolvemos el valor en decimal o flotante.

    return np.array( val1 ).astype( np.float64 )

# Empezamos a definir el algoritmo.

print( " --------------------------------------------------")

print( ' Verifique los valores ingresados. ' )

print( " --------------------------------------------------")


# Evaluamos la funcion en el punto inicial x0.

val2 = Obtener_evaluacion( x0 )  

# Obtenemos la norma de f( x0 ).

norma = np.linalg.norm( val2 ) 

# Checamos si la norma cumple con los requerimientos de ser menor que epsilon.

if( norma < epsilon ) :

    print( ' Norma de f( x0 ) : ' + str( norma ) + ' <= epsilon: ' +
          str( epsilon ) + '. Existe un punto x0 en la funcion. ' ) 
    
   # Salida del if.

    exit( 1 )

else :

    print( ' Lo siento su función no cumple las condiciones de Armijo - Wolfe. ' )

# Condiciones de Armijo - Wolfe.

# Definimos los valores de las variables.

a_i = alpha_1

iteracion = x0

d = - 1 * Obtener_evaluacion( x0 )

# Checamos las restricciones del algoritmo.

# Imprimimos en terminal los resultados.

while ( norma >= epsilon ) :
    
    print( " --------------------------------- " )

    print( " Resultados : " )
    
    print( " Cheque los valores obtenidos. " )

    print( ' Armijo - Wolfe. ' )

    print( ' Alpha´s : ' + str( a_i ) )

    print( ' Punto : ' + str( iteracion ) )

    print( ' d´s : ' + str( d ) )
    
    print( " --------------------------------- " )

    # Evaluamos la funcion.

    f_val = Evaluar( iteracion )

    print( ' f( x ) - evaluada : ' + str( f_val ) )

    Al = alpha_1 * beta_1 * \
      np.dot( Obtener_evaluacion( iteracion ) , d )

    print( ' Algoritmo : ' + str( Al ) )

    Armijo = f_val + Al

    print( ' Armijo : ' + str( Armijo ) )
    
    # Implementamos el algoritmo : x_i + alpha * d - direccion. 

    valor_a = iteracion + a_i * d 

    print( ' Iteraciones de alpha : ' + str( valor_a ) )

    # Evaluuamos la funcion obtenida arriba, es decir:

    # F( x_i + alpha * d )

    # Imprimimos en terminal los resultados.

    Armijo_val = Evaluar( valor_a ) 
    
    print( " --------------------------------------------------")

    print( ' Armijo iteraciones de alpha : ' + str( Armijo_val ) ) 
              
    print( " --------------------------------------------------")

    # Checamos las restricciones.

    if( Armijo >= Armijo_val ) :
        
        print( " --------------------------------------------------")

        print( ' Armijo - Wolfe - Valores - Itarciones. ' ) 

        print( ' Alpha iteraciones : ' + str( a_i ) )

        print(' Valor punto : ' + str( iteracion ) )

        print( ' d´s : ' + str( d ) )
        
        print( " --------------------------------------------------")
         
        # Condiciones de Wolfe.

        fx_val = Obtener_evaluacion( iteracion )  

        Wolfe = beta_2 * np.dot( fx_val , d )

        Wolfe_val = np.dot( Obtener_evaluacion( valor_a ) , d )
           
        print( " --------------------------------------------------")

        print( ' Wolfe - condiciones : ' + str( Wolfe ) )

        print( ' Valores de Wolfe : ' + str( Wolfe_val ) )
            
        print( " --------------------------------------------------")

        # Checamos las condiciones de Wolfe.

        # Con sus restricciones.

        # Imprimimos los resultados en terminal.

        if( Wolfe_val >= Wolfe ) :

            print( " --------------------------------------------------")

            print( ' Valores de Wolfe : ' )

            print( ' Valor de x_i + alpha * d : ' + str( iteracion ) )

            print( ' Tamaño de paso de alpha : ' + str( a_i ) )

            print( ' Dirección de descenso : ' + str( d ) )

            print( " --------------------------------------------------")


            # Volvemos x_i + alpha * d

            iteracion = valor_a

            # Elegimos alpha = 1

            a_i = alpha_1 

            # Checamos la funcion objetivo y la direccion de descenso.

            # direccion d.

            fx_val = Obtener_evaluacion( iteracion )

            d = - 1 * Obtener_evaluacion( iteracion )

            # Sacamos la norma de la funcion evaluada.

            norma = np.linalg.norm( fx_val )

            # Imprimimos los resultados en terminal.

            print( " ------------------------------------------------- " )

            print( ' Criterios : ' )

            print( ' f( x ) - evaluada : ' + str( fx_val ) )

            print( ' Norma de la función evaluada : ' + str( norma ) )

            print( 'Su epsilon es : ' + str( epsilon ) )

            print( " ------------------------------------------------- " )


        else :

            print( " ------------------------------------------------- " )

            print( ' Lo siento, no cumple las condiciones de Wolfe. ' )

            a_i = a_i * ep

            print( ' Punto : ' + str( a_i ) )

            print( " ------------------------------------------------- " )


    else :
        
        print( " ------------------------------------------------- " )

        print( ' Lo siento, no cumple con las condiciones de Armijo. ' ) 

        a_i = a_i * ep

        print( ' Punto : ' + str( a_i ) )
        
        print( " ------------------------------------------------- " )

    IT = IT + 1

print( " ------------------------------------------------- " )

print( 'Su numero de iteraciones es : ' + str( IT ) )

print( " -------------------------------------------------- ")
