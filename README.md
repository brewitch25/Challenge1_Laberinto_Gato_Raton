
Voy a crear un juego que se llama el laberinto del gato y del raton, decidi mantener el juego lo mas simple posible para poder dividir en bloques y asi estructurar bien el codigo

 ### << === >> DEFINIR TERRENO DE JUEGO << === >> ###
 # ------> Bloque1: Creacion terreno de juego <------
En el primer bloque se crea el tablero de juego, una matriz bidimensional de tamaño 5x5, defini los personajes del juego que son el gato, el raton y los espacios vacios del tablero, que estan representados por ".". 
Se crea una funcion llamada crear_terreno, lo que hace es crea una lista de listas con puntos que representa los espacios vacios, se ubica al gato en la posicion superior izquierda del tablero y al raton se le ubica en la posicion inferior derecha del tablero

# ------> Bloque2: Movimiento de personajes <------
En el segundo bloque se creo una funcion, llamado mover_personaje, dentro de esta funcion se define que el movimiento va a ser en 4 direcciones(arriba, abajo, izquierda, derecha), utilizando coordenadas, que son filas y columnas, en el bloque de codigo "cambio de posicion" el personaje, va a calcular donde ir, sin moverse todavia de su posicion inicial, en la porcion de codigo "verificacion de movimiento", en el "if" vemos si es que el movimiento a realizar se encuentra dentro de los limites del tablero, si esta dentro del rango del movimiento del tablero, se movera, en el "else", te dice que "el movimiento esta de los limites"

### << === >> SIMULACION DE MOVIMIENTO << === >> ###
# ------> Bloque3: movimientos al azar del gato y del raton <------- 
En el tercer bloque se va hacer que el gato y el raton se muevan de forma aleatoria, para eso se va a usar la libreria random, en esta porcion de bloque se va usar la funcion movimientos_al_azar, que que utiliza random.choice, porque elige los elementos de una lista aleatoriamente, el nombre de la lista es opciones_direcciones, dentro de la funcion movimientos_al_azar, ya los dos personajes se mueven de forma aleatoria.

### << === >> CONDICIONES DE FINALIZACION << === >> ###
Vamos a hacer primeramente la condicion de finalizacion, de manera sencilla, cada personaje va a tener 4 turnos disponible para hacer un movimiento, decidi utilizar el bucle for, especificamente "range", de 1 al 9, utilice el operador matematico % (modulus), para definir de esta forma el turno del gato y del raton, que va de la siguiente forma:
  => Turno del raton impar: % de los numeros impares que estan dentro del rango 1 al 9
  => Turno del gato par: % de los numeros pares que estan dentro del rango del 1 al 9
Se utilizo tambien el tipo de dato, boolean, para saber si el raton fue atrapado, y de esta forma poder saber si el juego termino antes de los 8 turnos