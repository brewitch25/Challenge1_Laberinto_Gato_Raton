
import random       # ---> Se va usar para los movimientos al azar(Bloque3)

### << === >> DEFINIR TERRENO DE JUEGO << === >> ###
## ==== Bloque1: Generacion de tablero de juego ===== ##

# Simbolos utilizados en el juego
VACIO = "."
GATO = "🐱"
RATON = "🐭"

# Creacion del terreno de juego, == matrix 5x5 ==
def crear_terreno():
    terreno = []     # Creacion de lista vacia
    for fila in range(4):    
        terreno.append([VACIO] * 4)  # Lista de lista con 5 puntos
    terreno[0][0] = GATO        # Posicion del gato en esquina superior izq
    terreno[3][3] = RATON       # Posiion raton esquina inferior derecha
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
    
    # Verificamos que el movimiento esté dentro de los límites (0 a 3)
    if 0 <= nueva_f < 4 and 0 <= nueva_c < 4:
        personaje = terreno[fila_actual][col_actual]
        terreno[fila_actual][col_actual] = VACIO # Deja el rastro vacío
        terreno[nueva_f][nueva_c] = personaje    # Se coloca en la nueva celda
        return nueva_f, nueva_c # Devolvemos la nueva posición para actualizar variables
    else:
        print("¡Movimiento fuera de los límites!")
        return fila_actual, col_actual
    
### << === >> SIMULACION DE MOVIMIENTO << === >> ###
## ==== Bloque3: movimento al azar del raton ==== ##

# Utlizamos el terreno, que ya esta creada las lineas 27

# Definimos las variables del ratón
# En la funcion crear_terreno se ubico al raton en la posicion [3][3] = RATON, empezamos ahí:
raton_f = 3
raton_c = 3

# Definimos las opciones de movimiento
opciones_direcciones = ["arriba", "abajo", "izquierda", "derecha"]

# Se usa la funcion random.choice, que usa una lista(opciones_direcciones) para elegir los elementos de la lista al azar
direccion_azar = random.choice(opciones_direcciones)

# Reutilizamos la funcion mover_personaje(Bloque2), y guardamos la posicion que nos devuelva la funcion
raton_f, raton_c = mover_personaje(terreno, raton_f, raton_c, direccion_azar)

# Mostramos el resultado en la terminal
# mostrar_terreno(terreno)


### << === >> CONDICIONES DE FINALIZACION << === >> ###
# Utilizando ya las variables definidad arriba, que son las posiciones, raton_f, raton_c, y la 
# lista de opciones_direcciones, se crea el bucle for para los turnos (4 turnos), inicialmente
for turno in range(4):
    print(f"Turno n°: {turno + 1}")         # Saber el turno
    direccion_azar = random.choice(opciones_direcciones)        # Se selecciona direccion al aza
    raton_f, raton_c = mover_personaje(terreno, raton_f, raton_c, direccion_azar)   # Movemos el personaje
    mostrar_terreno(terreno)                # ver como quedo el tablero en este turno

# En el caso que el raton escapo despues de 4 turnos
print("El raton ha escapado despues de 4 turnos!")


