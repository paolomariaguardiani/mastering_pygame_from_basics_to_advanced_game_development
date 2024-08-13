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

# Initalize font
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)

# Render text
text_surface = font.render("Hello, PyGame!", True, (0,0,0))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
            else:
                print("You missed the button!")

    # Clear screen
    screen.fill((255,255,255))

    # Draw shapes
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen, (255,0,0), (200,200), 40)
    pygame.draw.line(screen, (0,255,0), (300, 300), (400,400), 5)

    # Draw text
    screen.blit(text_surface, (100,100))

    # Draw button 
    button_rect = pygame.Rect(300,250,200,50)
    # print(button_rect.x, button_rect.y)
    pygame.draw.rect(screen, (0,128,255), button_rect)
    text_surface = font.render('Click Me', True, (255,255,255))
    screen.blit(text_surface, (button_rect.x + 50, button_rect.y + 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60) # 60 frames per second!

# Quit PyGame
pygame.quit()
sys.exit()



