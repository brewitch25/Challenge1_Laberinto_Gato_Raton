# =============================================================================
# README — terreno_de_juego.py
# Juego: Laberinto del Gato y el Ratón
# =============================================================================


DESCRIPCIÓN GENERAL
-------------------
Este módulo define el tablero (terreno de juego) para el juego "Laberinto del
Gato y el Ratón". Representa una cuadrícula 2D donde se mueven los personajes
y se colocan los elementos del juego.


SÍMBOLOS DEL TABLERO
--------------------
  '.'  → Celda vacía / libre
  '#'  → Pared (infranqueable)
  'R'  → Ratón (jugador o agente)
  'G'  → Gato (enemigo)
  'Q'  → Queso (objetivo del ratón)
  'S'  → Salida del laberinto


CLASE PRINCIPAL: Tablero
-------------------------
Representa el tablero completo como una lista de listas de strings.
Requiere mínimo 4x4 celdas al crearse.

  Métodos de inicialización:
  ┌──────────────────────────────────────────────────────────────────┐
  │ cargar_predefinido(estructura)                                   │
  │   Carga un tablero definido manualmente como lista de listas.    │
  │   Útil para niveles fijos o pruebas controladas.                 │
  ├──────────────────────────────────────────────────────────────────┤
  │ generar_aleatorio(prob_pared=0.25)                               │
  │   Genera un tablero procedural:                                  │
  │   - El borde exterior siempre es pared.                          │
  │   - Las celdas interiores tienen prob_pared de ser pared.        │
  │   - Ratón, Gato, Queso y Salida se colocan aleatoriamente        │
  │     en celdas libres del interior.                               │
  └──────────────────────────────────────────────────────────────────┘

  Métodos de acceso:
    obtener_celda(fila, col)        → devuelve el símbolo en esa posición
    establecer_celda(fila, col, v)  → escribe un símbolo en esa posición
    (ambos validan que la posición esté dentro del tablero)

  Visualización:
    mostrar()   → imprime el tablero en consola con leyenda de símbolos
    __str__()   → representación en texto plano (filas separadas por \\n)
    __repr__()  → resumen compacto, ej: Tablero(8x10)


FLUJO DE EJECUCIÓN (demo en __main__)
--------------------------------------
  1. Crea un Tablero 5x5 y carga una estructura predefinida → lo muestra.
  2. Crea un Tablero 8x10 aleatorio con 20 % de paredes → lo muestra.
  3. Crea un Tablero 12x15 aleatorio con 30 % de paredes → lo muestra.


ERRORES MANEJADOS
------------------
  - Tablero menor de 4x4                         → ValueError
  - Estructura predefinida con dimensiones incorrectas → ValueError
  - prob_pared fuera del rango [0.0, 1.0)        → ValueError
  - Celdas libres insuficientes para los elementos → ValueError
  - Acceso a posición fuera del tablero           → IndexError
"""
