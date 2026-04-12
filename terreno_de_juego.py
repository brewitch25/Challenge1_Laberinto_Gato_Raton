
import random       # ---> Se va usar para los movimientos al azar(Bloque3)
import copy         # ---> Se usa en el bloque de minimax
### << === >> DEFINIR TERRENO DE JUEGO << === >> ###
## ==== Bloque1: Generacion de tablero de juego ===== ##

# Simbolos utilizados en el juego
VACIO = "🌾"
GATO = "🐱"
RATON = "🐭"
CANTIDAD_DE_FILAS = 5
CANTIDAD_DE_COLUMNAS = 5

# Creacion del terreno de juego, == matriz 5x5 ==
def crear_terreno():
    terreno = []                      # Creacion de lista vacia
    for fila in range(CANTIDAD_DE_FILAS):     
        terreno.append([VACIO] * CANTIDAD_DE_COLUMNAS)          # Lista de lista con 5 puntos
    terreno[1][1] = GATO                                        # Posicion gato en la posicion superior izq
    terreno[3][3] = RATON                                       # Posicion raton en la posicion inferior derecha
    return terreno

# Mostrar matriz en la pantalla
def mostrar_terreno(terreno):
    for fila in terreno:
        print(" ".join(fila))

# Programa principal
terreno = crear_terreno()
# mostrar_terreno(terreno)

## ====== Bloque2: Movimiento de personajes ====== ##

# Función para mover un personaje (G o R)
# [Descripcion de la funcion]
#
# Params:
# - [param1]: [tipo] - [desc. de param]
# - [param2]: [tipo] - [desc. de param]
#
# Returns:
# [tipo] - Desc.
def mover_personaje(terreno, fila_actual, col_actual, direccion):
    # Definimos cuánto sumar/restar según la dirección
    movimientos = {
        "arriba": (-1, 0),          
        "abajo": (1, 0),
        "izquierda": (0, -1),
        "derecha": (0, 1)
    }
    
    # Obtenemos el cambio de posición
    
    df, dc = movimientos[direccion]
    nueva_f = fila_actual + df
    nueva_c = col_actual + dc
    
    # Verificamos que el movimiento esté dentro de los límites (0 a 5)
    if 0 <= nueva_f < CANTIDAD_DE_FILAS and 0 <= nueva_c < CANTIDAD_DE_COLUMNAS:
        personaje = terreno[fila_actual][col_actual]
        terreno[fila_actual][col_actual] = VACIO    # Deja el rastro vacío
        terreno[nueva_f][nueva_c] = personaje       # Se coloca en la nueva celda
        return nueva_f, nueva_c                     # Devolvemos la nueva posición para actualizar variables
    else:
        # print("¡Movimiento fuera de los límites!")
        return fila_actual, col_actual
    
### << === >> SIMULACION DE MOVIMIENTO << === >> ###
## ==== Bloque3: movimento al azar del raton ==== ##

# Utlizamos el terreno, que ya esta creado en el bloque1

# Definimos las variables del ratón y del gato
# Definimos la posicion del raton
#raton_fila = 3
#raton_columna = 3
# Definimos la posicion del gato
#gato_fila = 1
#gato_columna = 1

# Definimos las opciones de movimiento
opciones_direcciones = ["arriba", "abajo", "izquierda", "derecha"]

# # Funcion que hace que los personajes se muevan al azar 
# def movimientos_al_azar(personaje_f, personaje_c):
#     # El raton se mueve aleatoriamente
#     dir_personaje = random.choice(opciones_direcciones)
#     nuevo_personaje_f, nuevo_personaje_c = mover_personaje(terreno, personaje_f, personaje_c, dir_personaje)


#     return nuevo_personaje_f, nuevo_personaje_c


# # << ==== >> Aca empezamos a jugar y aplicamos las condiciones de finalizacion << ==== >>

# # Variable para saber si el raton fue atrapado
# atrapado = False
# # Creamos el bucle en rango 1 al 9, 4 turnos para cada personaje
# for turno in range(1, 9):  
#     print(f"Turno nº: {turno}")

#     # Turno del raton (impares):
#     if turno % 2 != 0:
#         print(f"Turno del 🐭")
#         raton_fila, raton_columna = movimientos_al_azar(raton_fila, raton_columna)

#     else:
#         print(f"Turno del 🐱")
#         gato_fila, gato_columna = movimientos_al_azar(gato_fila, gato_columna)
#     # Mostramos el tablero despues de cada movimiento
#     mostrar_terreno(terreno)

#     # Vemos si el gato y el raton estan en la misma posicion
#     if raton_fila == gato_fila and raton_columna == gato_columna:
#         print("El gato atrapo al raton!")
#         atrapado = True
#         break

# # Si el gato no atrapo al raton en los 4 turnos
# if not atrapado:
#     print("El raton logro escapar! Termino el juego!")


