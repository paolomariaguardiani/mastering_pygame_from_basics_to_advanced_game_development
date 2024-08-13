import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Shapes")

# Set up game clock
clock = pygame.time.Clock()
# print(clock.get_time, clock.get_rawtime)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255,255,255))

    # Draw shapes
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen, (255,0,0), (200,200), 40)
    pygame.draw.line(screen, (0,255,0), (300, 300), (400,400), 5)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60) # 60 frames per second!

# Quit PyGame
pygame.quit()
sys.exit()



