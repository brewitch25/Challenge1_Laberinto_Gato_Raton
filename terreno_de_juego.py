import random

# --- Símbolos del tablero ---
VACIO  = '.'   # Celda libre
PARED  = '#'   # Obstáculo infranqueable
QUESO  = 'Q'   # Objetivo del ratón
GATO   = 'G'   # Posición del gato
RATON  = 'R'   # Posición del ratón
SALIDA = 'S'   # Salida del laberinto

ELEMENTOS_UNICOS = [RATON, GATO, QUESO, SALIDA]


class Tablero:
    """Tablero bidimensional para el juego Laberinto del Gato y el Ratón.

    Internamente usa una lista de listas de strings (símbolos).
    Soporta dos modos de inicialización:
      - cargar_predefinido(): a partir de una estructura hardcoded
      - generar_aleatorio(): generación procedural con paredes aleatorias
    """

    def __init__(self, filas: int, columnas: int):
        if filas < 4 or columnas < 4:
            raise ValueError("El tablero debe tener al menos 4x4 celdas")
        self.filas = filas
        self.columnas = columnas
        self.cuadricula: list[list[str]] = self._crear_vacio()

    # ------------------------------------------------------------------
    # Construcción interna
    # ------------------------------------------------------------------

    def _crear_vacio(self) -> list[list[str]]:
        """Devuelve una cuadrícula nueva rellena de celdas vacías."""
        return [[VACIO] * self.columnas for _ in range(self.filas)]

    def _posiciones_interiores_libres(self) -> list[tuple[int, int]]:
        """Lista de celdas interiores (sin borde) que están vacías."""
        return [
            (f, c)
            for f in range(1, self.filas - 1)
            for c in range(1, self.columnas - 1)
            if self.cuadricula[f][c] == VACIO
        ]

    def _colocar_elementos_unicos(self, posiciones: list[tuple[int, int]]) -> None:
        """Coloca ratón, gato, queso y salida en posiciones libres dadas."""
        if len(posiciones) < len(ELEMENTOS_UNICOS):
            raise ValueError(
                "No hay suficientes celdas libres para colocar todos los elementos. "
                "Reduce la probabilidad de paredes o aumenta el tamaño del tablero."
            )
        for elemento, (f, c) in zip(ELEMENTOS_UNICOS, posiciones):
            self.cuadricula[f][c] = elemento

    # ------------------------------------------------------------------
    # Modos de inicialización
    # ------------------------------------------------------------------

    def cargar_predefinido(self, estructura: list[list[str]]) -> None:
        """Carga el tablero desde una lista de listas predefinida.

        Args:
            estructura: lista de listas de símbolos con dimensiones
                        iguales a (self.filas x self.columnas).

        Example:
            tablero.cargar_predefinido([
                ['#', '#', '#', '#', '#'],
                ['#', 'R', '.', 'Q', '#'],
                ['#', '.', '#', '.', '#'],
                ['#', 'G', '.', 'S', '#'],
                ['#', '#', '#', '#', '#'],
            ])
        """
        if len(estructura) != self.filas:
            raise ValueError(
                f"La estructura tiene {len(estructura)} filas pero el tablero tiene {self.filas}"
            )
        for i, fila in enumerate(estructura):
            if len(fila) != self.columnas:
                raise ValueError(
                    f"La fila {i} tiene {len(fila)} columnas pero el tablero tiene {self.columnas}"
                )

        self.cuadricula = [list(fila) for fila in estructura]

    def generar_aleatorio(self, prob_pared: float = 0.25) -> None:
        """Genera un tablero aleatorio.

        El borde exterior siempre será pared.  Las celdas interiores
        tienen una probabilidad 'prob_pared' de ser pared.
        Ratón, gato, queso y salida se colocan en posiciones libres
        elegidas al azar.

        Args:
            prob_pared: probabilidad (0.0-1.0) de que una celda interior
                        sea pared. Por defecto 0.25.
        """
        if not 0.0 <= prob_pared < 1.0:
            raise ValueError("prob_pared debe estar en el rango [0.0, 1.0)")

        self.cuadricula = self._crear_vacio()

        # Borde exterior → paredes
        for f in range(self.filas):
            for c in range(self.columnas):
                if f == 0 or f == self.filas - 1 or c == 0 or c == self.columnas - 1:
                    self.cuadricula[f][c] = PARED

        # Interior → paredes aleatorias
        for f in range(1, self.filas - 1):
            for c in range(1, self.columnas - 1):
                if random.random() < prob_pared:
                    self.cuadricula[f][c] = PARED

        # Colocar elementos únicos en posiciones libres mezcladas
        libres = self._posiciones_interiores_libres()
        random.shuffle(libres)
        self._colocar_elementos_unicos(libres)

    # ------------------------------------------------------------------
    # Acceso a celdas
    # ------------------------------------------------------------------

    def _validar_posicion(self, fila: int, col: int) -> None:
        if not (0 <= fila < self.filas and 0 <= col < self.columnas):
            raise IndexError(
                f"Posición ({fila}, {col}) fuera del tablero {self.filas}x{self.columnas}"
            )

    def obtener_celda(self, fila: int, col: int) -> str:
        self._validar_posicion(fila, col)
        return self.cuadricula[fila][col]

    def establecer_celda(self, fila: int, col: int, valor: str) -> None:
        self._validar_posicion(fila, col)
        self.cuadricula[fila][col] = valor

    # ------------------------------------------------------------------
    # Visualización
    # ------------------------------------------------------------------

    def mostrar(self) -> None:
        """Imprime el tablero en consola con separación entre celdas."""
        ancho = self.columnas * 2 - 1
        print(f"\n  Tablero {self.filas}x{self.columnas}")
        print("  " + "-" * ancho)
        for fila in self.cuadricula:
            print("  " + " ".join(fila))
        print("  " + "-" * ancho)
        print(f"  {RATON}=Ratón  {GATO}=Gato  {QUESO}=Queso  {SALIDA}=Salida  {PARED}=Pared  {VACIO}=Vacío\n")

    def __str__(self) -> str:
        return "\n".join(" ".join(fila) for fila in self.cuadricula)

    def __repr__(self) -> str:
        return f"Tablero({self.filas}x{self.columnas})"

    # ------------------------------------------------------------------
    # Posiciones de inicio fijas
    # Coloca al Gato en la esquina interior superior-izquierda (1,1) y
    # al Ratón en la esquina interior inferior-derecha (filas-2, cols-2).
    # Limpia las celdas previas de ambos actores antes de reubicarlos.
    # ------------------------------------------------------------------

    def establecer_posiciones_inicio(self) -> None:
        """Fija las posiciones de inicio canónicas de Gato y Ratón.

        - Gato  → esquina interior superior-izquierda (fila 1, col 1)
        - Ratón → esquina interior inferior-derecha   (fila filas-2, col columnas-2)

        Si alguno de los dos actores ya estaba colocado en el tablero,
        su celda anterior se deja vacía antes de moverlo.
        """
        # Limpiar posiciones anteriores del gato y el ratón (si existen)
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.cuadricula[f][c] in (GATO, RATON):
                    self.cuadricula[f][c] = VACIO

        # Esquina interior superior-izquierda → Gato
        self.cuadricula[1][1] = GATO

        # Esquina interior inferior-derecha → Ratón
        self.cuadricula[self.filas - 2][self.columnas - 2] = RATON


# ----------------------------------------------------------------------
# Demo
# ----------------------------------------------------------------------

if __name__ == "__main__":

    # --- Tablero predefinido 5x5 ---
    print("=== Tablero predefinido (5x5) ===")
    t1 = Tablero(5, 5)
    t1.cargar_predefinido([
        ['#', '#', '#', '#', '#'],
        ['#', 'R', '.', 'Q', '#'],
        ['#', '.', '#', '.', '#'],
        ['#', 'G', '.', 'S', '#'],
        ['#', '#', '#', '#', '#'],
    ])
    t1.mostrar()

    # --- Tablero aleatorio 8x10 ---
    print("=== Tablero aleatorio (8x10) ===")
    t2 = Tablero(8, 10)
    t2.generar_aleatorio(prob_pared=0.20)
    t2.mostrar()

    # --- Tablero aleatorio 12x15 ---
    print("=== Tablero aleatorio (12x15) ===")
    t3 = Tablero(12, 15)
    t3.generar_aleatorio(prob_pared=0.30)
    t3.mostrar()
