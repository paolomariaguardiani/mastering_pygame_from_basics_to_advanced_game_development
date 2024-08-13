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

        keys = pygame.key.get_pressed()
        # print(keys)
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
               
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