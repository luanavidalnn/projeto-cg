import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Projeção de Quadrado com Pygame")

# Cores
GRID_COLOR = (200, 200, 200)
AXIS_COLOR = (0, 0, 0)
SQUARE_COLOR = (0, 0, 255)
TEXT_COLOR = (0, 0, 0)

# Configuração da malha quadriculada
GRID_SPACING = 20

# Função para calcular as coordenadas DC (Device Coordinates)
def dc_coordinates(x, y):
    dc_x = WINDOW_SIZE[0] // 2 + x * GRID_SPACING
    dc_y = WINDOW_SIZE[1] // 2 - y * GRID_SPACING
    return dc_x, dc_y

# Função para converter DC em NDC
def ndc_coordinates(dc_x, dc_y):
    ndc_x = (dc_x - WINDOW_SIZE[0] // 2) / GRID_SPACING
    ndc_y = -(dc_y - WINDOW_SIZE[1] // 2) / GRID_SPACING
    return ndc_x, ndc_y

def draw_grid():
    for x in range(0, WINDOW_SIZE[0], GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_SIZE[1]))
    for y in range(0, WINDOW_SIZE[1], GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_SIZE[0], y))

# Entrada do usuário para as coordenadas
x_min = float(input("Digite o valor de x mínimo: "))
x_max = float(input("Digite o valor de x máximo: "))
y_min = float(input("Digite o valor de y mínimo: "))
y_max = float(input("Digite o valor de y máximo: "))

# Calcular as coordenadas DC do quadrado
dc_x_min, dc_y_max = dc_coordinates(x_min, y_max)
dc_x_max, dc_y_min = dc_coordinates(x_max, y_min)

# Calcular as coordenadas NDC do quadrado
ndc_x_min, ndc_y_max = ndc_coordinates(dc_x_min, dc_y_max)
ndc_x_max, ndc_y_min = ndc_coordinates(dc_x_max, dc_y_min)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preencher a tela com uma cor de fundo
    screen.fill((255, 255, 255))  # Branco

    draw_grid()

    # Desenhar os eixos x e y
    pygame.draw.line(screen, AXIS_COLOR, (0, WINDOW_SIZE[1] // 2), (WINDOW_SIZE[0], WINDOW_SIZE[1] // 2))
    pygame.draw.line(screen, AXIS_COLOR, (WINDOW_SIZE[0] // 2, 0), (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1]))

    # Desenhar o quadrado projetado
    square_rect = pygame.Rect(dc_x_min, dc_y_min, dc_x_max - dc_x_min, dc_y_max - dc_y_min)
    pygame.draw.rect(screen, SQUARE_COLOR, square_rect)

    # Exibir valores na tela
    font = pygame.font.Font(None, 30)
    text_lines = [
        f"x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}",
        f"DC: ({dc_x_min}, {dc_y_max}), ({dc_x_max}, {dc_y_min})",
        f"NDC: ({ndc_x_min:.2f}, {ndc_y_max:.2f}), ({ndc_x_max:.2f}, {ndc_y_min:.2f})"
    ]

    for i, line in enumerate(text_lines):
        text = font.render(line, True, TEXT_COLOR)
        screen.blit(text, (10, 10 + i * 30))

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
