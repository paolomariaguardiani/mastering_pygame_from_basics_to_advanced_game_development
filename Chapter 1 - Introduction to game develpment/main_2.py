import pygame
import sys

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My First PyGame Window")

# Drawing Shapes and Text
# Set up font
font = pygame.font.SysFont(None, 48)


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

    # Draw a red rectangle
    # One tuple is for the color RGB, the second tuple is for x, y, width, height
    pygame.draw.rect(screen, (255,0,0), (100,100,200,100)) 
    # # pygame.draw.rect(screen, (255,0,0), (screen.get_width() / 2, screen.get_height() / 2,200,100))

    # Render and display text
    text = font.render("Hello, Pygame!", True, (0,0,0)) # True = antialiasing
    screen.blit(text, (100,250))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
