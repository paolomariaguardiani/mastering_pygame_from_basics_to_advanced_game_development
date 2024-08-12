import pygame
import sys
# Initialize PyGame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My PyGame Window")

# Set up game clock
clock = pygame.time.Clock()

# lista_di_eventi = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((0,0,0))

    # lista_di_eventi.append(event)

    # Update display
    pygame.display.flip()

    # Cap the grame rate
    clock.tick(60) # 60 frames per second

# for event in lista_di_eventi:
#     print(event)

# Quit Pygame
pygame.quit()
sys.exit()
