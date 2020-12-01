import pygame
import connect4 as c4
import ai_algorithms

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# GAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
game = c4.ConnectFour()

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
DG = (75, 75, 75)
RED = (255, 70, 70)
BLUE = (32, 69, 189)
YELLOW = (255,255,70)

# SHAPES + SIZES
SQ = 86  # 100, 120

chip_centers = {}

game_mode = "intro"

settings = {
    'players': 1,
    'size': "5x6",
    'mode': 'easy',
    'SQ': 120,
    'CIRC': 55,
    'SQ_WIDTH': 720,
    'SQ_HEIGHT': 720,
    'gap':40
}

def intro_screen(): 
    global game_mode, game
    screen.fill(WHITE)
    font = pygame.font.Font(None, 70)
    text = font.render("Connect Four", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 200))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 40)

    if settings['players'] == 1:
        one_player_text = font.render("One Player", True, DG)
        two_player_text = font.render("Two Player", True, GRAY)
        start_text = font.render("NEXT", True, GRAY)
    else: 
        one_player_text = font.render("One Player", True, GRAY)
        two_player_text = font.render("Two Player", True, DG)
        start_text = font.render("START GAME", True, GRAY)
    
    one_player_rect = one_player_text.get_rect(center=(300, SCREEN_HEIGHT/2))
    two_player_rect = two_player_text.get_rect(center=(500, SCREEN_HEIGHT/2))
    screen.blit(one_player_text, one_player_rect)
    screen.blit(two_player_text, two_player_rect)
    
    if settings['size'] == "5x6":
        five_six_text = font.render("5x6", True, DG)
        six_seven_text = font.render("6x7", True, GRAY)
        seven_eight_text = font.render("7x8", True, GRAY)
        
    elif settings['size'] == "6x7":
        five_six_text = font.render("5x6", True, GRAY)
        six_seven_text = font.render("6x7", True, DG)
        seven_eight_text = font.render("7x8", True, GRAY)
        
    elif settings['size'] == "7x8":
        five_six_text = font.render("5x6", True, GRAY)
        six_seven_text = font.render("6x7", True, GRAY)
        seven_eight_text = font.render("7x8", True, DG)

    five_six_rect = five_six_text.get_rect(center=(300, 350))
    six_seven_rect = six_seven_text.get_rect(center=(400, 350))
    seven_eight_rect = seven_eight_text.get_rect(center=(500, 350))
    screen.blit(five_six_text, five_six_rect)
    screen.blit(six_seven_text, six_seven_rect)
    screen.blit(seven_eight_text, seven_eight_rect)

    
    start_rect = start_text.get_rect(center=(400, 425))
    screen.blit(start_text, start_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if one_player_rect.collidepoint(event.pos):
                    settings['players'] = 1
                elif two_player_rect.collidepoint(event.pos):
                    settings['players'] = 2
                elif five_six_rect.collidepoint(event.pos):
                    game = c4.ConnectFour(5,6)
                    settings['size'] = "5x6"
                    settings['SQ'] = 120
                    settings['CIRC'] = settings['SQ'] // 2 - 5
                    settings['SQ_WIDTH'] = game.COLS * settings['SQ']
                    settings['SQ_HEIGHT'] = game.ROWS+1 * settings['SQ']
                    settings['gap'] = 40
                    
                elif six_seven_rect.collidepoint(event.pos):
                    game = c4.ConnectFour(6,7)
                    settings['size'] = "6x7"
                    settings['SQ'] = 100
                    settings['CIRC'] = settings['SQ'] // 2 - 5
                    settings['SQ_WIDTH'] = game.COLS * settings['SQ']
                    settings['SQ_HEIGHT'] = game.ROWS+1 * settings['SQ']
                    settings['gap'] = 50
                    
                elif seven_eight_rect.collidepoint(event.pos):
                    game = c4.ConnectFour(7,8)
                    settings['size'] = "7x8"
                    settings['SQ'] = 86
                    settings['CIRC'] = settings['SQ'] // 2 - 5
                    settings['SQ_WIDTH'] = game.COLS * settings['SQ']
                    settings['SQ_HEIGHT'] = game.ROWS+1 * settings['SQ']
                    settings['gap'] = 56
                    
                elif start_rect.collidepoint(event.pos):
                    if settings['players'] == 1:
                        game_mode = 'levels'
                    else:
                        game_mode = 'two_players'
                    print('start game')
                
	
def levels(): 
    global game_mode, running
    screen.fill(WHITE)
    font = pygame.font.Font(None, 70)
    text = font.render("Choose a Level", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 200))
    screen.blit(text, text_rect)
    font = pygame.font.Font(None, 40)

    if settings['mode'] == 'easy':
        easy = font.render("Easy", True, DG)
        med = font.render("Medium", True, GRAY)
        hard = font.render("Hard", True, GRAY)
    elif settings['mode'] == 'medium':
        easy = font.render("Easy", True, GRAY)
        med = font.render("Medium", True, DG)
        hard = font.render("Hard", True, GRAY)
    elif settings['mode'] == 'hard':
        easy = font.render("Easy", True, GRAY)
        med = font.render("Medium", True, GRAY)
        hard = font.render("Hard", True, DG)
    
    start_text = font.render("START GAME", True, GRAY)
    start_rect = start_text.get_rect(center=(400, 425))

    easy_rect = easy.get_rect(center=(SCREEN_WIDTH/2, 275))
    med_rect = med.get_rect(center=(SCREEN_WIDTH/2, 318))
    hard_rect = hard.get_rect(center=(SCREEN_WIDTH/2, 360))

    screen.blit(easy, easy_rect)
    screen.blit(med, med_rect)
    screen.blit(hard, hard_rect)
    screen.blit(start_text, start_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if easy_rect.collidepoint(event.pos):
                    settings['mode'] = 'easy'
                elif med_rect.collidepoint(event.pos):
                    settings['mode'] = 'medium'
                elif hard_rect.collidepoint(event.pos):
                    settings['mode'] = 'hard'
                elif start_rect.collidepoint(event.pos):
                    if settings['mode'] == 'easy':
                        game_mode = 'easy'
                    elif settings['mode'] == 'medium':
                        game_mode = 'medium'
                    elif settings['mode'] == 'hard':
                        game_mode = 'hard'

def draw_board():
    screen.fill(WHITE)
    board = pygame.Rect(0, 0, game.COLS * settings['SQ'], game.ROWS * settings['SQ'])
    board.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, BLUE, board)
    
    for col in range(game.COLS):
        for row in range(game.ROWS):
            circle_pos = (int(col * settings['SQ'] + settings['SQ'] // 2 + board.left), int(row * settings['SQ'] + settings['SQ'] / 2))
            chip_centers[(col, row)] = circle_pos
            if game.board[row][col] == 0:
                pygame.draw.circle(screen, YELLOW, circle_pos, settings['CIRC'])
            elif game.board[row][col] == 1:
                pygame.draw.circle(screen, RED, circle_pos, settings['CIRC'])
            else:
                pygame.draw.circle(screen, BLACK, circle_pos, settings['CIRC'])

def easy():
    global game_mode, running
    from random import randint

    if game.winner is not None:
        game_mode = "end"
    
    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_mode = "intro"
                game.reset()
        if event.type == pygame.QUIT:
            running = False
        
        if game.turn == 1:
            col = randint(0,game.COLS-1)
            row = game.make_move(col)

            if row: 
                draw_board()
                pygame.display.update()

        else: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    col = (event.pos[0] - settings['gap']) // settings['SQ'] 
                    row = game.make_move(col)
                    
                    if row:
                        draw_board()
                        pygame.display.update()

def medium():
    global game_mode, running
    if game.winner is not None:
        game_mode = "end"

    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_mode = "intro"
                game.reset()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = (event.pos[0] - settings['gap']) // settings['SQ']  
                row = game.make_move(col)

                if row:
                    draw_board()
                    pygame.display.update()

    if game.winner is not None:
        game_mode = "end"
        print(game)
    elif game.turn == 1:
        game_state = ai_algorithms.GameState(game)
        row = game.make_move(ai_algorithms.expectimax(game_state)[1])
        if row:
            draw_board()
            pygame.display.update()

def hard():
    global game_mode
    global running
    if game.winner is not None:
        game_mode = "end"

    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_mode = "intro"
                game.reset()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = (event.pos[0] - settings['gap']) // settings['SQ']  
                row = game.make_move(col)

                if row:
                    draw_board()
                    pygame.display.update()

    if game.winner is not None:
        game_mode = "end"
        print(game)
    elif game.turn == 1:
        game_state = ai_algorithms.GameState(game)
        row = game.make_move(ai_algorithms.minimax(game_state)[1])
        if row:
            draw_board()
            pygame.display.update()



def two_players():
    global game_mode, running
    if game.winner is not None:
        game_mode = "end"
    screen.fill(WHITE)
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_mode = "intro"
                game.reset()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = (event.pos[0] - settings['gap']) // settings['SQ']  
                row = game.make_move(col)
                turn = game.turn
                pygame.draw.circle(screen, RED, (500,500), settings['CIRC'])
                pygame.display.update()
                if row:
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
            win = "Yellow"
        elif game.winner == 1: 
            win = "Red"
        else:
            win = "No one"
        text = font.render(win + " won!", True, BLACK)

    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 200))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 40)
    play_again = font.render("Play again", True, DG)
    pa_rect = play_again.get_rect(center=(SCREEN_WIDTH/2, 300))
    screen.blit(play_again, pa_rect)

    main_screen = font.render("Back to Main Menu", True, DG)
    ms_rect = main_screen.get_rect(center=(SCREEN_WIDTH/2, 350))
    screen.blit(main_screen, ms_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ms_rect.collidepoint(event.pos):
                    game_mode = "intro"
                    game.reset()
                elif pa_rect.collidepoint(event.pos):
                    game.reset()
                    if settings['players'] == 1:
                        game_mode = settings['mode']
                    else:
                        game_mode = 'two_players'


while running:
    if game_mode == "intro":
        intro_screen()
    elif game_mode == "levels":
        levels()
    elif game_mode == "easy":
        easy()
    elif game_mode == "medium":
        medium()
    elif game_mode == "hard":
        hard()
    elif game_mode == "two_players":
        two_players()
    elif game_mode == "end":
        end_screen()
        
    pygame.display.flip()


pygame.quit()
