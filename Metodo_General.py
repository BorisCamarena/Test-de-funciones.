# Implementamos el Metodo General para Armijo y Wolfe.

def Metodo_General( f , g , H , xk ) :

  m_a = 500

  ro = 0.55

  ep1 = 0.4

  k = 0

  epsilon = 1e-5

  while k < m_a :

    gk = g( xk )

    Hk = H( xk )

    dk = -1.0 * np.linalg.solve( Hk , gk )

    if np.linalg.norm( dk ) < epsilon :

      break

    m = 0

    mk = 0

    while m < 20 :

      if Armijo( gk , dk , xk , ro**m , ep1 ) :

        mk = m

        break

      m += 1

    xk += ro**mk * dk

    k += 1

  print( " Resultado del Metodo. " )

  print( " El punto xk = " , xk )

  print( " La funcion evaluada f( xk ) = " , round(f( xk ) , 3 ) )

  print( " Numero de iteraciones es : " , k )
