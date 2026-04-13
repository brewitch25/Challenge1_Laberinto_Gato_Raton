
Voy a crear un juego que se llama el laberinto del gato y del raton, que implemente el algoritmo MiniMax, decidi mantener el juego lo mas simple posible para poder dividir en bloques y asi estructurar bien el codigo.

  # <===> Archivo terreno_de_juego.py <===>
Se creo una carpeta para la creacion de los archivos del juego, la carpeta fue dividida en 2 archivos, el archivo "terreno_de_jueg.py", basicamente en él se define las constantes de los personajes del gato y del raton, el espacio vacio, las dimensiones del tablero, que usa fila y columnas

 # ==> Funcion crear_terreno <==
 En esta funcion se crea el terreno de juego, donde se crea el tablero con usando lista de lista, tambien se posiciona a los personajes dentro del tablero, para finalmente, mostrar el terreno de juego (tablero).
 # ==> Funcion mover_personaje <==
 Aca basicamente se mueve al personaje en 4 direccion posibles(arriba, abajo, izquierda, derecha), tambien se establecen los limites para que los personajes no salgan del tablero de juego.

 Luego se hacen la implementacion de los movimientos aleatorios para ver si los personajes se mueven dentro del tablero

  # <===> Archivo MinMax.py <===>
  En este archivo se implementa el algoritmo minimax, decidi hacer en un archivo separado para entender mejor el codigo, se hizo que los personajes jueguen uno contra otro (maquina vs maquina), en este archivo se hace la importacion y reutilizacion de de las funciones y constantes ya creadas en el archivo terreno_de_juego.py, se creo una variable estado_inicial, el cual ya posiciona a los personajes y crea el tablero, se hace una uso de una funcion de la libreria copy, que es copy.deepcopy, para no modificar el estado de juego, tambien se crearon las funciones que definen los casos bases(finalizacion del juego) del algoritmo minimax. Tambien se creo la funion del calculo de distancia para implementar en el algoritmo.
  Para la implementacion del algoritmo, tomo un poco de tiempo investigar y definir cuales eran los elementos que tenia que formar parte del algoritmo, ya que se implemento el formato de maquina vs maquina, lo que funiono de manera inmediata fue la implementacion del caso base, lo que tomo un poco de tiempo fue entender como hacer que cada personaje logre moverse, utilizando ya la funcion mover_personaje y aplicarlo de forma independiente para el gato y para el raton, lo que note tambien fue la eliminacion de una funcion que escribi y despues me di cuenta que no iba a necesitar en el algoritmo, 


