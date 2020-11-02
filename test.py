import pygame
import pygame.freetype 

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# GAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_FONT = pygame.freetype.Font("./bebas/Bebas-Regular.ttf", 24)
running = True

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

while running:
    screen.fill(WHITE)
    font = pygame.font.Font(None, 70)
    text = font.render("Connect Four", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 2*SCREEN_HEIGHT/5))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 40)
    one_player_text = font.render("One Player", True, BLACK)
    one_player_rect = one_player_text.get_rect(center=(3*SCREEN_WIDTH/8, SCREEN_HEIGHT/2))
    screen.blit(one_player_text, one_player_rect)

    two_player_text = font.render("Two Players", True, BLACK)
    two_player_rect = two_player_text.get_rect(center=(5*SCREEN_WIDTH/8, SCREEN_HEIGHT/2))
    screen.blit(two_player_text, two_player_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if one_player_rect.collidepoint(event.pos):
                print('player 1')  # change to AI gameplay
            elif two_player_rect.collidepoint(event.pos):
                print('player 2')  # regular gameplay
        
    
    pygame.display.flip()

pygame.quit()