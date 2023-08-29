import pygame
import pygame_gui
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
WINDOW_SIZE = (1080, 760)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("COMPUTAÇÃO GRÁFICA")

# Cores
GRID_COLOR = (200, 200, 200)
AXIS_COLOR = (0, 0, 0)
SQUARE_COLOR = (0, 0, 255)
TEXT_COLOR = (0, 0, 0)

# Configuração da malha quadriculada
GRID_SPACING = 10

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

# Inicialização do pygame_gui
gui_manager = pygame_gui.UIManager(WINDOW_SIZE)

# Definição dos rótulos para as caixas de entrada
label_x_min = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((5, 10), (80, 30)),
    text="x_min:",
    manager=gui_manager,
)
label_x_max = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((5, 50), (80, 30)),
    text="x_max:",
    manager=gui_manager,
)
label_y_min = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((5, 90), (80, 30)),
    text="y_min:",
    manager=gui_manager,
)
label_y_max = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((5, 130), (80, 30)),
    text="y_max:",
    manager=gui_manager,
)

# Definição das caixas de entrada usando pygame_gui
input_x_min = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((85, 10), (140, 30)),
    manager=gui_manager
)
input_x_max = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((85, 50), (140, 30)),
    manager=gui_manager
)
input_y_min = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((85, 90), (140, 30)),
    manager=gui_manager
)
input_y_max = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((85, 130), (140, 30)),
    manager=gui_manager
)

# Definição do botão
enter_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((85, 180), (80, 30)),  # Ajuste a posição vertical aqui
    text="Enter",
    manager=gui_manager
)

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
                x_min = float(input_x_min.get_text().strip())
                x_max = float(input_x_max.get_text().strip())
                y_min = float(input_y_min.get_text().strip())
                y_max = float(input_y_max.get_text().strip())

    gui_manager.update(time_delta)
    
    # Preencher a tela com uma cor de fundo
    screen.fill((255, 255, 255))  # Branco

    draw_grid()
    
    
    # Desenhar rótulos nos eixos
    font = pygame.font.Font(None, 24)

    x_label = font.render("x", True, TEXT_COLOR)
    x_label_rect = x_label.get_rect(center=(WINDOW_SIZE[0] - 15, WINDOW_SIZE[1] // 2 + 20))
    screen.blit(x_label, x_label_rect)

    y_label = font.render("y", True, TEXT_COLOR)
    y_label_rect = y_label.get_rect(center=(WINDOW_SIZE[0] // 2 + 20, 15))
    screen.blit(y_label, y_label_rect)
    
    # Desenhar setas nos eixos
    arrow_size = 10
    
    # Seta no eixo x positivo
    pygame.draw.polygon(
        screen,
        AXIS_COLOR,
        [(WINDOW_SIZE[0] - arrow_size, WINDOW_SIZE[1] // 2 - arrow_size),
        (WINDOW_SIZE[0], WINDOW_SIZE[1] // 2),
        (WINDOW_SIZE[0] - arrow_size, WINDOW_SIZE[1] // 2 + arrow_size)]
    )

    # Seta no eixo y positivo
    pygame.draw.polygon(
        screen,
        AXIS_COLOR,
        [(WINDOW_SIZE[0] // 2 - arrow_size, arrow_size),
        (WINDOW_SIZE[0] // 2, 0),
        (WINDOW_SIZE[0] // 2 + arrow_size, arrow_size)]
    )

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

    # Exibir valores na tela
    small_font = pygame.font.Font(None, 20)
    text_position_y = WINDOW_SIZE[1] - 50

    text_lines = [
        f"x_min: {x_min:.2f}, x_max: {x_max:.2f}, y_min: {y_min:.2f}, y_max: {y_max:.2f}",
        f"DC: ({dc_x_min:.2f}, {dc_y_max:.2f}), ({dc_x_max:.2f}, {dc_y_min:.2f})",
        f"NDC: ({ndc_x_min:.2f}, {ndc_y_max:.2f}), ({ndc_x_max:.2f}, {ndc_y_min:.2f})"
    ]

    for i, line in enumerate(text_lines):
        text = small_font.render(line, True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, text_position_y + i * 20))
        screen.blit(text, text_rect)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
