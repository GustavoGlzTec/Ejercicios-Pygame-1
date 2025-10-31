import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sesión 3 - Mini: Rectángulo con rastro")

BG = (24, 26, 34)
RECT_COLOR = (0, 160, 255)
TRAIL_COLOR = (200, 220, 255)
rect = pygame.Rect(380, 290, 40, 40)
speed = 5

# Soporte (opcional) para joystick/control
pygame.joystick.init()
joy = pygame.joystick.Joystick(0) if pygame.joystick.get_count() > 0 else None
if joy:
    joy.init()

trail = []          # lista de posiciones (centros)
TRAIL_MAX = 500     # límite para no crecer sin control

clock = pygame.time.Clock()
running = True

def clamp_rect(r):
    if r.left < 0: r.left = 0
    if r.top < 0: r.top = 0
    if r.right > WIDTH: r.right = WIDTH
    if r.bottom > HEIGHT: r.bottom = HEIGHT

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Movimiento con teclado
    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy += speed

    # Movimiento con joystick (si existe)
    if joy:
        ax = joy.get_axis(0)   # izquierda-derecha
        ay = joy.get_axis(1)   # arriba-abajo
        dead = 0.15
        if abs(ax) > dead: dx += int(ax * speed * 2.5)
        if abs(ay) > dead: dy += int(ay * speed * 2.5)

    rect.x += dx
    rect.y += dy
    clamp_rect(rect)

    # Guardar posición en el rastro (centro del rectángulo)
    trail.append(rect.center)
    if len(trail) > TRAIL_MAX:
        trail.pop(0)

    # Dibujo
    WIN.fill(BG)

    # Dibujar rastro de círculos pequeños
    # (opcional: hacer que los últimos sean más brillantes)
    for i, (cx, cy) in enumerate(trail):
        pygame.draw.circle(WIN, TRAIL_COLOR, (cx, cy), 4)

    pygame.draw.rect(WIN, RECT_COLOR, rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
