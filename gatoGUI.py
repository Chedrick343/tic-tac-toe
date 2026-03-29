import pygame
import sys
import minimax
# ------------------ CONFIG ------------------

WIDTH, HEIGHT = 500, 600
CELL_SIZE = 100

# ------------------ JUEGO ------------------

tablero = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

turno = "X"

# ------------------ GUI ------------------

def main():
    global turno

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gato")

    font = pygame.font.SysFont(None, 40)
    small_font = pygame.font.SysFont(None, 28)
    clock = pygame.time.Clock()

    # Inputs
    input_fila = ""
    input_col = ""
    activo = None

    fila_rect = pygame.Rect(120, 500, 60, 30)
    col_rect = pygame.Rect(220, 500, 60, 30)
    boton_rect = pygame.Rect(320, 500, 100, 30)

    def dibujar_texto(texto, x, y, f=font):
        img = f.render(texto, True, (0, 0, 0))
        screen.blit(img, (x, y))

    def dibujar_tablero():
        for i in range(3):
            for j in range(3):
                x = j * CELL_SIZE + 100
                y = i * CELL_SIZE + 100

                pygame.draw.rect(screen, (0, 0, 0), (x, y, CELL_SIZE, CELL_SIZE), 2)

                # 🔥 Solo dibuja si NO es None
                if tablero[i][j] is not None:
                    dibujar_texto(tablero[i][j], x + 35, y + 25)

    def colocar():
        nonlocal input_fila, input_col
        global turno

        if input_fila.isdigit() and input_col.isdigit():
            f = int(input_fila)
            c = int(input_col)

            if 0 <= f < 3 and 0 <= c < 3:
                # 🔥 Validar casilla vacía con None
                if tablero[f][c] is None:
                    tablero[f][c] = turno
                    turno = "O" if turno == "X" else "X"

        input_fila = ""
        input_col = ""
    def colocarAI():
        global turno
        jugada = minimax.ai_play(tablero)
        c,f = jugada
        if tablero[f][c] is None:
            tablero[f][c] = turno
            turno = "O" if turno == "X" else "X"
    # ---------------- LOOP ----------------

    while True:
        screen.fill((255, 255, 255))
        if(turno == "X"):
            colocarAI()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if fila_rect.collidepoint(event.pos):
                    activo = "fila"
                elif col_rect.collidepoint(event.pos):
                    activo = "col"
                elif boton_rect.collidepoint(event.pos):
                    colocar()
                else:
                    activo = None

            if event.type == pygame.KEYDOWN and activo:
                if event.key == pygame.K_BACKSPACE:
                    if activo == "fila":
                        input_fila = input_fila[:-1]
                    else:
                        input_col = input_col[:-1]
                else:
                    if activo == "fila":
                        input_fila += event.unicode
                    else:
                        input_col += event.unicode

        # ---------------- DIBUJO ----------------

        # Título
        dibujar_texto("Gato", 200, 20)

        # Tablero
        dibujar_tablero()

        # Labels
        dibujar_texto("Fila:", fila_rect.x - 60, fila_rect.y + 5, small_font)
        dibujar_texto("Col:", col_rect.x - 50, col_rect.y + 5, small_font)

        # Inputs
        pygame.draw.rect(screen, (200, 200, 200), fila_rect, 2)
        pygame.draw.rect(screen, (200, 200, 200), col_rect, 2)

        dibujar_texto(input_fila, fila_rect.x + 10, fila_rect.y + 3, small_font)
        dibujar_texto(input_col, col_rect.x + 10, col_rect.y + 3, small_font)

        # Botón
        pygame.draw.rect(screen, (0, 150, 0), boton_rect)
        dibujar_texto("Colocar", boton_rect.x + 10, boton_rect.y + 5, small_font)

        # Turno
        dibujar_texto(f"Turno: {turno}", 180, 450, small_font)

        pygame.display.flip()
        clock.tick(60)


# ------------------ MAIN ------------------

if __name__ == "__main__":
    main()