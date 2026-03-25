Voy a crear un juego que se llama el laberinto del gato y del raton, decidi mantener el juego lo mas simple posible para poder dividir en bloques y asi estructurar bien el codigo

 ### << === >> DEFINIR TERRENO DE JUEGO << === >> ###
 # ------> Bloque1: Creacion terreno de juego <------
En el primer bloque se crea el tablero de juego, una matriz bidimensional de tamaño 4x4, se definio los personajes del juego que son el gato, el raton y los espacios vacios del tablero, que estan representados por ".". 
Se crea una funcion llamada crear_terreno, lo que hace es crea una lista de listas con puntos que representa los espacios vacios, se ubica al gato en la posicion superior izquierda del tablero y al raton se le ubica en la posicion inferior derecha del tablero

# ------> Bloque2: Movimiento de personajes <------
En el segundo bloque se creo una funcion, llamado mover_personaje, dentro de esta funcion se define que el movimiento va a ser en 4 direcciones(arriba, abajo, izquierda, derecha), utilizando coordenadas, que son filas y columnas, en el porcion del bloque de codigo "cambio de posicion" el personaje, va a calcular donde ir, sin moverse todavia de su posicion inicial, en la porcion de codigo "verificacion de movimiento", en el "if" vemos si es que el movimiento a realizar se encuentra dentro de los limites del tablero, si esta dentro del rango del movimiento del tablero, se movera, en el "else", te dice que "el movimiento esta de los limites"

### << === >> SIMULACION DE MOVIMIENTO << === >> ###
# ------> Bloque3: movimientos ala azar del raton <------- 
En el tercer bloque se va hacer que el raton se mueva de forma aleatoria, para eso se va a usar la libreia random, en esta porcion de bloque se va usar la funcion random.choice, porque elige los elementos de una lista aleatoriamente, tambien se vuelve a llamar a la funcion mover_personaje, que basicamente hace que se muevan los personajes, usando su posicion ya definida en las filas y las columnas en conjunto con la funcion direccion al azar, que decide aleatoriamente la poscion y finalmente se muestra el resultado en la terminal
