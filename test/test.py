import pygame
import pygame_gui
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Projeção de Quadrado com Pygame GUI")

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

# Função para desenhar a malha quadriculada
def draw_grid():
    for x in range(0, WINDOW_SIZE[0], GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_SIZE[1]))
    for y in range(0, WINDOW_SIZE[1], GRID_SPACING):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_SIZE[0], y))

# Inicialização do pygame_gui
gui_manager = pygame_gui.UIManager(WINDOW_SIZE)

# Definição das caixas de entrada usando pygame_gui
input_x_min = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((10, 10), (140, 30)),
    manager=gui_manager
)
input_x_max = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((10, 50), (140, 30)),
    manager=gui_manager
)
input_y_min = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((10, 90), (140, 30)),
    manager=gui_manager
)
input_y_max = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((10, 130), (140, 30)),
    manager=gui_manager
)

# Definição do botão
enter_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((160, 130), (80, 30)),
    text="Enter",
    manager=gui_manager
)

# Lista de caixas de entrada
input_elements = [input_x_min, input_x_max, input_y_min, input_y_max]

# Variáveis para armazenar os valores de entrada
x_min = 0.0
x_max = 0.0
y_min = 0.0
y_max = 0.0

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        gui_manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == enter_button:
                for input_element in input_elements:
                    if input_element == input_x_min:
                        x_min = float(input_element.get_text())
                    elif input_element == input_x_max:
                        x_max = float(input_element.get_text())
                    elif input_element == input_y_min:
                        y_min = float(input_element.get_text())
                    elif input_element == input_y_max:
                        y_max = float(input_element.get_text())

    gui_manager.update(time_delta)
    
    # Preencher a tela com uma cor de fundo
    screen.fill((255, 255, 255))  # Branco

    draw_grid()

    # Desenhar UI
    gui_manager.draw_ui(screen)

    # Realizar os cálculos com os valores de entrada
    dc_x_min, dc_y_max = dc_coordinates(x_min, y_max)
    dc_x_max, dc_y_min = dc_coordinates(x_max, y_min)
    ndc_x_min, ndc_y_max = ndc_coordinates(dc_x_min, dc_y_max)
    ndc_x_max, ndc_y_min = ndc_coordinates(dc_x_max, dc_y_min)

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
