import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My First PyGame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Fill the screen with a color (e.g., white)
    screen.fill((255,255,255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
