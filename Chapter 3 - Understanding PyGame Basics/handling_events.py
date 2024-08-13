import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up display
width, height = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Event Handling")

# Set up game clock
clock = pygame.time.Clock()
print(clock.get_time())

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                print("Escape key pressed!")
            elif event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                print(f"Mouse clicked at {event.pos}")
        
        # Clear screen
        screen.fill((255,255,255))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Quit PyGame
pygame.quit()
sys.exit()