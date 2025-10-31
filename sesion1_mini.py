import pygame

pygame.init()
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini-proyecto: cambiar color con 'C'")

RED = (255, 0, 0)
BLUE = (0, 102, 255)

current_color = RED  # Inicia blanco

running = True
while running:
    for event in pygame.event.get():
        # Cerrar ventana o con Esc
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Cambiar color al presionar 'C' (mayúscula o minúscula)
            elif event.key == pygame.K_c:
                current_color = BLUE if current_color == RED else RED

    window.fill(current_color)
    pygame.display.flip()

pygame.quit()
