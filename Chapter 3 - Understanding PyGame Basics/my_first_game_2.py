import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")

# Set up the game clock to control the frame rate:
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # print(event)
    # Clear screen (each frame)
    screen.fill((255,255,255))

    # Draw a rectangle
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30,30,60,60))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit PyGame
pygame.quit()
sys.exit()

