import pygame
import pygame_gui
import sys

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projeção de Quadrado com Pygame")

# Cores
grid_color = (200, 200, 200)  # Cor da malha quadriculada
axis_color = (0, 0, 0)         # Cor dos eixos x e y
square_color = (0, 0, 255)     # Cor do quadrado
pixel_color = (255, 0, 0)      # Cor do pixel
text_color = (0, 0, 0)         # Cor do texto

# Configuração da malha quadriculada
grid_spacing = 20  # Espaçamento entre as linhas da malha

# Função para calcular as coordenadas DC (Device Coordinates)
def dc_coordinates(x, y):
    dc_x = width // 2 + x * grid_spacing
    dc_y = height // 2 - y * grid_spacing
    return dc_x, dc_y

# Função para converter DC em NDC
def ndc_coordinates(dc_x, dc_y):
    ndc_x = (dc_x - width // 2) / grid_spacing
    ndc_y = -(dc_y - height // 2) / grid_spacing
    return ndc_x, ndc_y

# Inicialização do Gerenciador de Interface de Usuário (UI)
ui_manager = pygame_gui.UIManager((width, height))

# Criar caixas de texto para as coordenadas
input_x_min = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(10, 10, 100, 30), manager=ui_manager)
input_x_max = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(10, 50, 100, 30), manager=ui_manager)
input_y_min = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(10, 90, 100, 30), manager=ui_manager)
input_y_max = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(10, 130, 100, 30), manager=ui_manager)

# Loop principal do jogo
# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Atualizar o gerenciador de UI
        ui_manager.process_events(event)

    # Atualizar os valores das coordenadas a partir das caixas de texto
    x_max_text = input_x_max.get_text()
    x_min_text = input_x_min.get_text()
    y_max_text = input_y_max.get_text()
    y_min_text = input_y_min.get_text()

# Verificar se as caixas de texto não estão vazias antes de converter para float
if x_max_text and x_min_text and y_max_text and y_min_text:
    x_max = float(x_max_text)
    x_min = float(x_min_text)
    y_max = float(y_max_text)
    y_min = float(y_min_text)

    # Preencher a tela com uma cor de fundo
    screen.fill((255, 255, 255))  # Branco

    # Desenhar a malha quadriculada
    for x in range(0, width, grid_spacing):
        pygame.draw.line(screen, grid_color, (x, 0), (x, height))
        # Exibir valores de x_max e x_min nos rótulos do eixo x
        if x == width // 2 + x_max * grid_spacing:
            font = pygame.font.Font(None, 20)
            text = font.render(f"{x_max:.1f}", True, text_color)
            screen.blit(text, (x + 2, height // 2 + 2))
        elif x == width // 2 + x_min * grid_spacing:
            font = pygame.font.Font(None, 20)
            text = font.render(f"{x_min:.1f}", True, text_color)
            screen.blit(text, (x + 2, height // 2 + 2))

    for y in range(0, height, grid_spacing):
        pygame.draw.line(screen, grid_color, (0, y), (width, y))
        # Exibir valores de y_max e y_min nos rótulos do eixo y
        if y == height // 2 - y_max * grid_spacing:
            font = pygame.font.Font(None, 20)
            text = font.render(f"{y_max:.1f}", True, text_color)
            screen.blit(text, (width // 2 + 2, y + 2))
        elif y == height // 2 - y_min * grid_spacing:
            font = pygame.font.Font(None, 20)
            text = font.render(f"{y_min:.1f}", True, text_color)
            screen.blit(text, (width // 2 + 2, y + 2))

    # Desenhar os eixos x e y
    pygame.draw.line(screen, axis_color, (0, height // 2), (width, height // 2))  # Eixo x
    pygame.draw.line(screen, axis_color, (width // 2, 0), (width // 2, height))  # Eixo y

    # Desenhar o quadrado projetado
    pygame.draw.rect(screen, square_color, pygame.Rect(dc_x_min, dc_y_min, dc_x_max - dc_x_min, dc_y_max - dc_y_min))

    # Desenhar o pixel
    pygame.draw.rect(screen, pixel_color, pygame.Rect(dc_pixel_x, dc_pixel_y, grid_spacing, grid_spacing))

    # Atualizar o gerenciador de UI
    ui_manager.update(1 / 60.0)

    # Renderizar o gerenciador de UI na tela
    ui_manager.draw_ui(screen)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
sys.exit()
