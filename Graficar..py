# Empezamos a graficar.

# Importamos las librerias.

print("Graficar.")

import matplotlib.pyplot as plt

import numpy as np

# Creamos el espacio lineal.

a = 40

b = 90

T = np.linspace( a , b , 100 )

# Planteamos la ecuacion.

U = ( 204165.5 ) / (330 - 2 * T ) * ( 10400 ) / ( T - 20 )

# Graficamos.

plt.figure( )

# Elegimos el color de la grafica.

# Y ploteamos.

plt.plot( T , U , 'k' )

plt.xlabel( 'Temperatura' )

plt.ylabel( 'Costo' )

plt.grid( )

plt.show( )
