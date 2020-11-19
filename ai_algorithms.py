# class GameState:
#
#     def __init__(self, game):
#         self.board = [row[:] for row in game.board]  # make a deep copy of the game board
#         self.turn = 0
#         self.ROWS = game.ROWS
#         self.COLS = game.COLS
#         self.PLAYERS = 2
#         self.winner = None
#         self.TO_WIN = game.TO_WIN
#
#     # I changed this is_win function so that it didn't rely on a specific row/column
#     def is_win(self, player):
#         for col in range(self.COLS):
#             c = 0
#             for row in range(self.ROWS):
#                 if self.board[row][col] == player:
#                     c += 1
#                     if c == self.TO_WIN:
#                         self.winner = player
#                         return True
#                 else:
#                     c = 0
#
#         # horizontal
#         for row in range(self.ROWS):
#             c = 0
#             for col in range(self.COLS):
#                 if self.board[row][col] == player:
#                     c += 1
#                     if c == self.TO_WIN:
#                         self.winner = player
#                         return True
#                 else:
#                     c = 0
#
#         # diagonal /
#         for col in range(self.COLS - (self.TO_WIN - 1)):
#             for row in range(self.ROWS - (self.TO_WIN - 1)):
#                 if self.board[row][col] == player and self.board[row + 1][col + 1] == player and self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
#                     return True
#
#         # diagonal \
#         for col in range(self.COLS - (self.TO_WIN - 1)):
#             for row in range(self.TO_WIN - 1, self.ROWS):
#                 if self.board[row][col] == player and self.board[row - 1][col + 1] == player and self.board[row - 2][col + 2] == player and self.board[row - 3][col + 3] == player:
#                     return True
#         return False
#
#     def is_tie(self):
#         for i in range(self.ROWS):
#             for j in range(self.COLS):
#                 if self.board[i][j] is None:
#                     return False
#         return True
#
#     def next_valid(self, col):
#         if self.board[0][col] is None:
#             for row in range(self.ROWS - 1, -1, -1):
#                 if self.board[row][col] is None:
#                     return row
#         return None
#
#     def get_successors(self):
#         successor_list = []  # list of coordinates
#         for col in range(self.COLS):
#             row = self.next_valid(col)
#             if row is not None:
#                 successor_list.append((row, col))
#         return successor_list
#
#     def get_score(self):  # will write this
#         # heuristic is based on the number of twos and threes in a row (for the computer)
#         # could implement different heuristics as part of report
#         return 1
#
#
# def minimax(game):
#     game_state = GameState(game)
#     return max_value(game_state, 0, 5)
#
#
# def max_value(game_state, num_moves, max_depth):
#     if game_state.is_win(1):
#         return [None, 100]  # computer wins
#     elif game_state.is_win(0):
#         return [None, -100]  # player wins
#     elif game_state.is_tie():
#         return [None, 0]  # not sure what score for tie should be
#     elif num_moves > max_depth:
#         return [None, game_state.get_score()]
#     cur_max = -999999999
#     move = None
#     # print(game_state.board)
#     # print(game_state.get_successors())
#     for successor in game_state.get_successors():
#         row = successor[0]
#         col = successor[1]
#         new_game_state = GameState(game_state)
#         new_game_state.board[row][col] = 1  # computer move
#         new_max = min_value(new_game_state, num_moves + 1, max_depth)[1]
#         if new_max >= cur_max:
#             cur_max = new_max
#             move = successor
#     return [move, cur_max]
#
#
# def min_value(game_state, num_moves, max_depth):
#     if game_state.is_win(1):
#         return [None, 100]  # computer wins
#     elif game_state.is_win(0):
#         return [None, -100]  # player wins
#     elif game_state.is_tie():
#         return [None, 0]  # not sure what score for tie should be
#     elif num_moves > max_depth:
#         return [None, game_state.get_score()]
#     cur_min = 999999999
#     move = None
#     for successor in game_state.get_successors():
#         row = successor[0]
#         col = successor[1]
#         new_game_state = GameState(game_state)
#         new_game_state.board[row][col] = 0  # player move
#         new_min = max_value(new_game_state, num_moves + 1, max_depth)[1]
#         if new_min <= cur_min:
#             cur_min = new_min
#             move = successor
#     return [move, cur_min]

from copy import deepcopy
from random import shuffle
from game import ConnectFour

class State(object):
        # def __init__(self, game):
        #     self.board = [row[:] for row in game.board]  # make a deep copy of the game board
        #     self.turn = 0
        #     self.ROWS = game.ROWS
        #     self.COLS = game.COLS
        #     self.PLAYERS = 2
        #     self.winner = None
        #     self.TO_WIN = game.TO_WIN

    def __init__(self, game_state):
        self.board = deepcopy(game_state.board)
        self.turn = 0
        self.ROWS = game_state.ROWS
        self.COLS = game_state.COLS
        self.PLAYERS = 2
        self.winner = None
        self.TO_WIN = game_state.TO_WIN

    def equals(self, state):
        obj = State()
        return obj == state

    # returns list of actions from current state
    # actions are ints represented by a column where token can be dropped
    def getLegalActions(self, board):
        actions = []
        for i in range(self.COLS):
            if board[0][i] is None:  # blank spot => valid action
                actions.append(i)
        return actions

    # returns successor as a State object
    def generateSuccessors(self, player, action):
        for row in range(self.ROWS):
            if self.board[row][action] != '1' and self.board[row][action] != '0':
                new_state = deepcopy(self.board)
                new_state.board[row-1][action] = player
        return new_state

    # def evaluate(self, gameState):
    #     if gameState.winner == 0:  # checks if state is terminal
    #         return [None, 100]
    #     elif gameState.winner == 1:
    #         return [None, -100]
    #     return [None, 0]

# class MiniMax(object):
#     def __init__(self, depth, alpha, beta):
#         self.depth = depth
#         self.alpha = alpha
#         self.beta = beta


    def minimax_alphabeta(self, gamestate, depth, player):
        # get possible actions first
        actions = gamestate.getLegalActions(self.board)
        # randomize and set best action and best score
        shuffle(actions)
        best_action = actions[0]
        best_score = float("-inf")

        alpha = float("inf")
        beta = float("-inf")

        if player == '0':
            opponent = '1'
        else:
            opponent = '0'

        # go through all boards
        for action in actions:
            # create temp board for all those moves and call min on that board
            temp_board = testgame.make_move(action)
            score = self.min_beta(temp_board, depth - 1, alpha, beta, player, opponent)

            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    def min_beta(self, board, depth, a, b, player, opponent):
        actions = []

        for col in range(self.COLS):
            if testgame.is_valid(col):
                temp_move = testgame.make_move(col)
                actions.append(temp_move)

        if depth == 0 or len(actions) == 0 or gamestate.winner is None:
            return 0
            # will need to return some value
        beta = b

        # for action in valid_actions:
        for action in actions:
            board_score = float("inf")

            if a < beta:
                temp_board = testgame.make_move(action)
                board_score = self.max_alpha(temp_board, depth - 1, a, beta, player, opponent)

            if board_score < beta:
                beta = board_score
        return float(beta)

    def max_alpha(self, board, depth, a, b, player, opponent):
        actions = []

        for col in range(self.COLS):
            if testgame.is_valid(col):
                temp_move = testgame.make_move(col)
                actions.append(temp_move)

        if depth == 0 or len(actions) == 0 or gamestate.winner is None:
            return 0
            # will need to return some value

        alpha = a

        # for action in actions:
        for action in actions:
            board_score = float("inf")

            if alpha < b:
                temp_board = testgame.make_move(action)
                board_score = self.min_beta(temp_board, depth - 1, alpha, b, player, opponent)

            if board_score > self.alpha:
                alpha = board_score
        return float(alpha)


testgame = ConnectFour()
gamestate = State(testgame)
print(gamestate.minimax_alphabeta(gamestate, 0, '0'))

