import pygame
import connect4 as game

pygame.init()
clock = pygame.time.Clock()

game = game.ConnectFour()

window = pygame.display.set_mode((game.COLS * 100, (game.ROWS + 1) * 100))


def draw_blank_board(game):  # works with every board size
    for i in range(game.COLS):
        for j in range(game.ROWS):
            # draw a blue rectangle at every spot
            pygame.draw.rect(window, (0, 0, 255), (i * 100, (j + 1) * 100, 100, 100))
            # draw a black circle at every spot
            pygame.draw.circle(window, (0, 0, 0), (i * 100 + 50, (j + 1) * 100 + 50), 47)


draw_blank_board(game)
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    draw_blank_board(game)
    pygame.display.update()
    clock.tick(30)