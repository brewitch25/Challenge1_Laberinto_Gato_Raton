

## ==== Bloque de generacion de tablero de juego ===== ##

# Simbolos utilizados en el juego
VACIO = "."
GATO = "G"
RATON = "R"

# Creacion del terreno de juego, == matrix 5x5 ==
def crear_terreno():
    terreno = []     # Creacion de lista vacia
    for fila in range(5):    
        terreno.append([VACIO] * 5)  # Lista de lista con 5 puntos
    terreno[0][0] = GATO        # Posicion del gato en esquina superior izq
    terreno[4][4] = RATON       # Posiion raton esquina inferior derecha
    return terreno

# Mostrar matriz en la pantalla
def mostrar_terreno(terreno):
    for fila in terreno:
        print(" ".join(fila))

# Programa principal
terreno = crear_terreno()
mostrar_terreno(terreno)
