import pygame
import math
import sys
import random

# Init
pygame.init()
WIDTH = 800  # Reduced from original size
HEIGHT = 400  # Reduced from original size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Projectile Motion Simulator ✨")
font = pygame.font.SysFont("Arial", 20)

# Colors
def rainbow_color(i):
    return (i % 360, 100, 50, 100)

# Vars
angle = 45
velocity = 100
gravity = 9.8
scale = 0.3
start_x = 50  # Keep this the same for left edge
start_y = HEIGHT - 50  # Adjust based on new height
time = 0
dt = 0.1
running = True
trajectory = []
reset = True

clock = pygame.time.Clock()

def draw_text(text, x, y):
    surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface, (x, y))

while running:
    clock.tick(60)
    screen.fill((10, 10, 40))  # Dark aesthetic background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Real-time Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        angle = min(angle + 1, 90)
    if keys[pygame.K_DOWN]:
        angle = max(angle - 1, 0)
    if keys[pygame.K_RIGHT]:
        velocity += 1
    if keys[pygame.K_LEFT]:
        velocity = max(1, velocity - 1)
    if keys[pygame.K_w]:
        gravity += 0.1
    if keys[pygame.K_s]:
        gravity = max(0.1, gravity - 0.1)
    if keys[pygame.K_r]:
        trajectory = []
        time = 0
        reset = True

    # Init on reset
    if reset:
        angle_rad = math.radians(angle)
        x = start_x
        y = start_y
        reset = False

    # Motion
    x = start_x + velocity * math.cos(angle_rad) * time
    y = start_y - (velocity * math.sin(angle_rad) * time - 0.5 * gravity * time ** 2)

    if y < HEIGHT:
        trajectory.append((int(x), int(y)))

    # Draw ball
    if y < HEIGHT:
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 8)

    # Draw colorful trail
    for i, point in enumerate(trajectory):
        color = pygame.Color(0)
        color.hsla = rainbow_color(i * 5)
        pygame.draw.circle(screen, color, point, 4)

    # UI
    draw_text(f"Angle: {angle}° (↑/↓)", 10, 10)
    draw_text(f"Velocity: {velocity} px/s (←/→)", 10, 40)
    draw_text(f"Gravity: {round(gravity, 1)} (W/S)", 10, 70)
    draw_text("Press 'R' to Reset", 10, 100)

    pygame.display.flip()
    time += dt

pygame.quit()
sys.exit()
