import copy         
from terreno_de_juego import VACIO, GATO, RATON, opciones_direcciones 
from terreno_de_juego import crear_terreno, mover_personaje, mostrar_terreno

profundidad = 4

estado_inicial = {"fila_raton": 1, 
                  "columna_raton": 1,
                  "fila_gato": 3,
                  "columna_gato": 3,
                  "terreno": crear_terreno()}


# Funcion para copiar el estado del juego, sin modificar la estructura original
def copiar_estado(estado_actual):
    return copy.deepcopy(estado_actual)

# Definimos cuando gana el gato 
def gato_gana(estado_actual):
    return estado_actual["fila_raton"] == estado_actual["fila_gato"] \
        and estado_actual["columna_raton"] == estado_actual["columna_gato"]    

# El juego termina si el gato atrapo al raton 
def termino_juego(estado_actual):
    return gato_gana(estado_actual)
# DEVUELVE UN BOOLEAN

# Evaluamos quien gano (+1 -> raton, -1 -> gato)
def ganador_o_perdedor(estado_actual):
    if gato_gana(estado_actual):
        return - 1       # GANO GATO
    else:
        return  1        # GANA RATON

# Funcion que retornar el estado despues de mover el raton (no modific el esrado actual) 
# Que recibe (estado_actual y direccion) => Que devuelve (la nuevo estado del raton en el tablero)
# Direccion: una de las 4 opciones (arriba, abajo, izquierda, derecha)
def mover_raton(estado_actual, direccion):
    nuevo_estado_raton = copiar_estado(estado_actual)
    nueva_fila, nueva_columna = mover_personaje(nuevo_estado_raton["terreno"], estado_actual["fila_raton"], 
                                                estado_actual["columna_raton"], direccion)
    nuevo_estado_raton["fila_raton"] = nueva_fila
    nuevo_estado_raton["columna_raton"] = nueva_columna
    return nuevo_estado_raton

# Funcion que retornar el estado despues de mover el gato(no modifica el estado actual)
# Que recibe (estado_actual, direccion) => Que devuelve (el nuevo estado del gato en el tablero)
# Direccion: una de las 4 opciones (arriba, abajo, izquierda, derecha)
def mover_gato(estado_actual, direccion):
    nuevo_estado_gato = copiar_estado(estado_actual)
    nueva_fila, nueva_columna = mover_personaje(nuevo_estado_gato["terreno"], estado_actual["fila_gato"], 
                                                estado_actual["columna_gato"], direccion)
    nuevo_estado_gato["fila_gato"] = nueva_fila
    nuevo_estado_gato["columna_raton"] = nueva_columna
    return nuevo_estado_gato

# Funcion de calculo de distancia (Manhattan), saber si se acerca o se aleja
def calcular_distancia(estado_actual):
    distancia_filas = abs(estado_actual["fila_raton"] - estado_actual["fila_gato"])
    distancia_columnas = abs(estado_actual["raton_columna"] - estado_actual["columna_gato"])
    return distancia_filas + distancia_columnas
    


# << ===== >> Funcion minmax << ===== >>
def min_max(estado_actual, profundidad_actual, turno_max):
    # -- Caso base - Cuando termina el juego -- 
    if profundidad_actual == 0 or termino_juego(estado_actual):
        return ganador_o_perdedor(estado_actual)

    # Turno maximizador 
    if turno_max:
        max_valor = float("-inf")           
        for direccion in opciones_direcciones:
            eval_raton =  min_max(mover_raton(estado_actual, direccion), profundidad_actual - 1, False)
            max_valor = max(max_valor, eval_raton)
        return max_valor

    # Turno minimizador
    else:
        min_valor = float("inf")
        for direccion in opciones_direcciones: 
            eval_gato = min_max(mover_gato(estado_actual, direccion), profundidad_actual - 1, True)
            min_valor = min(min_valor, eval_gato)
        return min_valor
    

# << === >> Juego min_max() << === >>

estado_de_juego = copy.deepcopy(estado_inicial)    


for turno in range(1, 21):           # => Rango de 1 a 9, 4 turnos para cada personaje
    print(f"Turno nº:{turno}")

    # Turno del maximizador(RATON)
    if turno % 2 != 0: 
        max_valor_raton = float("-inf")
        movimiento_elegido = None 
        for direccion in opciones_direcciones:
            estado_a_evaluar = mover_raton(estado_de_juego, direccion)  # => Crea un estado despues de moverse en una direccion
            resultado = min_max(estado_a_evaluar, profundidad, False)

            # Evaluamos si el movimiento a realizar, maximiza
            if resultado > max_valor_raton:
                max_valor_raton = resultado
                movimiento_elegido = direccion
        # Movemos al raton en la direccion elegida
        estado_de_juego = mover_raton(estado_de_juego, movimiento_elegido)        

    # Turno minimizador (GATO)
    else:
        min_valor_gato = float("inf")
        movimiento_elegido = None
        for direccion in opciones_direcciones:
            estado_a_evaluar = mover_gato(estado_de_juego, direccion)
            resultado = min_max(estado_a_evaluar, profundidad, True)

            #Evaluamos si el movimiento a realizar, minimiza
            if resultado < min_valor_gato:
                min_valor_gato = resultado
                movimiento_elegido = direccion  
        # MOvemos al gato con el movimiento con la direccion elegida
        estado_de_juego = mover_gato(estado_de_juego, movimiento_elegido)

# Mostramos el tablero despues de cada movimiento
    mostrar_terreno(estado_de_juego["terreno"])        # Preguntar si esta bien
