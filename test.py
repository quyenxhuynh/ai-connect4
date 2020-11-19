import pygame
import pygame.freetype 
import game

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# GAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_FONT = pygame.freetype.Font("./bebas/Bebas-Regular.ttf", 24)
game = game.ConnectFour()
running = True

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

# SHAPES + SIZES
SQ = 120
CIRC = SQ // 2 - 5
SQ_WIDTH = game.COLS * SQ
SQ_HEIGHT = game.ROWS+1 * SQ
chip_centers = {}

game_mode = "intro"

def draw_board():
    screen.fill(WHITE)
    board = pygame.Rect(0, 0, game.COLS * SQ, game.ROWS * SQ)
    board.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, BLUE, board)
    
    for col in range(game.COLS):
        for row in range(game.ROWS):
            circle_pos = (int(col * SQ + SQ // 2 + board.left), int(row * SQ + SQ / 2))
            chip_centers[(col, row)] = circle_pos
            if game.board[row][col] == 0:
                pygame.draw.circle(screen, RED, circle_pos, CIRC)
            elif game.board[row][col] == 1:
                pygame.draw.circle(screen, YELLOW, circle_pos, CIRC)
            else:
                pygame.draw.circle(screen, BLACK, circle_pos, CIRC)


def two_players():
    global game_mode

    if game.winner is not None:
        game_mode = "end"

    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = (event.pos[0] - 40) // SQ  # 40 to account for the white gap between screen.left and board.left
                row = game.make_move(col)
                turn = game.turn
                pygame.draw.circle(screen, RED, (500,500), CIRC)
                pygame.display.update()
                # print(game_mode, game.winner)
                if row:
                    draw_board()
        

def intro_screen(): 
    global game_mode
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
            global running
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if one_player_rect.collidepoint(event.pos):
                    print('player 1')  # change to AI gameplay
                elif two_player_rect.collidepoint(event.pos):
                    game_mode = 'two_player'
                    draw_board()

def end_screen():
    global game_mode
    screen.fill(WHITE)
    font = pygame.font.Font(None, 70)
    result = game.winner
    if result == 2:
        text = font.render("It was a tie.", True, BLACK)
    else:
        if game.winner == 0:
            win = "Red"
        else: 
            win = "Yellow"
        text = font.render(win + " won!", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 40)
    play_again = font.render("Play again", True, BLACK)
    pa_rect = play_again.get_rect(center=(SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/5))
    screen.blit(play_again, pa_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pa_rect.collidepoint(event.pos):
                    game.reset()
                    print('hi')
                    game_mode = "intro"

while running:
    # print(game_mode)
    if game_mode == "intro":
        intro_screen()
    elif game_mode == "two_player":
        two_players()
    elif game_mode == "end":
        end_screen()
        
        
    pygame.display.flip()


pygame.quit()
