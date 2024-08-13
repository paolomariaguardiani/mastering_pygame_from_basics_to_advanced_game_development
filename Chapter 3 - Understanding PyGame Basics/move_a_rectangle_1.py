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

# Character position
x, y = width // 2, height // 2
speed = 5

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
                x -= speed
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button
                print(f"Mouse clicked at {event.pos}")
        
        # Clear screen
        screen.fill((255,255,255))

        # Draw rectangle
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60,60))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

# Quit PyGame
pygame.quit()
sys.exit()