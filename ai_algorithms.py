class GameState:

    def __init__(self, game, DANGERFACTOR = 0):
        self.board = [row[:] for row in game.board]  # make a deep copy of the game board
        self.turn = 1
        self.ROWS = game.ROWS
        self.COLS = game.COLS
        self.PLAYERS = 2
        self.winner = None
        self.TO_WIN = game.TO_WIN
        self.DANGERFACTOR = DANGERFACTOR

    # I changed this is_win function so that it didn't rely on a specific row/column
    def is_win(self, player):
        for col in range(self.COLS):
            c = 0
            for row in range(self.ROWS):
                if self.board[row][col] == player:
                    c += 1
                    if c == self.TO_WIN:
                        # self.winner = player
                        return True
                else:
                    c = 0

        # horizontal
        for row in range(self.ROWS):
            c = 0
            for col in range(self.COLS):
                if self.board[row][col] == player:
                    c += 1
                    if c == self.TO_WIN:
                        # self.winner = player
                        return True
                else:
                    c = 0

        # diagonal /
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.ROWS - (self.TO_WIN - 1)):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player and self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
                    return True

        # diagonal \
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.TO_WIN - 1, self.ROWS):
                if self.board[row][col] == player and self.board[row - 1][col + 1] == player and self.board[row - 2][col + 2] == player and self.board[row - 3][col + 3] == player:
                    return True
        return False

    def is_tie(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j] is None:
                    return False
        return True

    def next_valid(self, col):
        if self.board[0][col] is None:
            for row in range(self.ROWS - 1, -1, -1):
                if self.board[row][col] is None:
                    return row
        return None

    def get_successors(self):
        successor_list = []  # list of coordinates
        for col in range(self.COLS):
            row = self.next_valid(col)
            if row is not None:
                successor_list.append((row, col))
        return successor_list

    def dangerous_good_h(self, DANGERFACTOR):
        ai_slots = 0
        human_slots = 0
        empty_slots_col = 0
        empty_slots_row = 0
        empty_slots_posdiag = 0
        empty_slots_negdiag = 0

        max_allowable_perc = 0.3
        DANGERFACTOR = DANGERFACTOR

        # col
        for col in range(self.COLS):
            for row in range(self.ROWS):
                if self.board[row][col] == 1:
                    ai_slots += 1

                    if human_slots/4 >= max_allowable_perc:
                        perc_won = human_slots/4
                        dangerousforai_col = perc_won * (DANGERFACTOR/max_allowable_perc)
                        DANGERFACTOR += dangerousforai_col

                elif self.board[row][col] == 0:
                    human_slots += 1

                    if ai_slots / 84 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_col = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_col
                else:
                    empty_slots_col += 1


        # row
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_row = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_row

                elif self.board[row][col] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_row = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_row

                else:
                    empty_slots_row += 1

        # diagonal /
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.ROWS - (self.TO_WIN - 1)):
                if self.board[row][col] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        self.DANGERFACTOR += dangerousforai_posdiag

                if self.board[row + 1][col + 1] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_posdiag

                if self.board[row + 2][col + 2] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_posdiag

                if self.board[row][col] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_posdiag

                if self.board[row + 1][col + 1] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_posdiag

                if self.board[row + 2][col + 2] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_posdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_posdiag

                else:
                    empty_slots_posdiag += 1

        # diagonal \
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.TO_WIN - 1, self.ROWS):
                if self.board[row][col] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_negdiag
                if self.board[row - 1][col + 1] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_negdiag

                if self.board[row - 2][col + 2] == 1:
                    ai_slots += 1

                    if human_slots /4 >= max_allowable_perc:
                        perc_won = human_slots / 4
                        dangerousforai_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforai_negdiag


                if self.board[row][col] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_negdiag

                if self.board[row - 1][col + 1] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_negdiag

                if self.board[row - 2][col + 2] == 0:
                    human_slots += 1

                    if ai_slots /4 >= max_allowable_perc:
                        perc_won = ai_slots / 4
                        dangerousforh_negdiag = perc_won * (DANGERFACTOR / max_allowable_perc)
                        DANGERFACTOR += dangerousforh_negdiag

                else:
                    empty_slots_negdiag += 1

        return -1 * (self.DANGERFACTOR/100)

    def get_score(self):

        ai_twos = 0  # num of two-in-a-rows
        ai_threes = 0  # num of three-in-a-rows
        player_twos = 0
        player_threes = 0
        
        for col in range(self.COLS):
            ai_score = 0
            player_score = 0
            for row in range(self.ROWS):
                middle = self.COLS//2
                if self.board[row][middle] == 1 and ai_score == 0:
                    ai_score += 1
                if self.board[row][col] == 1:
                    ai_score += 1
                    if ai_score == 2:
                        ai_twos += 1
                    if ai_score == 3:
                        ai_threes += 1
                else:
                    ai_score = 0
                if self.board[row][col] == 0:
                    player_score += 1
                    if player_score == 2:
                        player_twos += 1
                    if player_score == 3:
                        player_threes += 1
                else:
                    player_score = 0

        for row in range(self.ROWS):
            ai_score = 0
            player_score = 0
            for col in range(self.COLS):
                if self.board[row][col] == 1:
                    ai_score += 1
                    if ai_score == 2:
                        ai_twos += 1
                    if ai_score == 3:
                        ai_threes += 1
                else:
                    ai_score = 0
                if self.board[row][col] == 0:
                    player_score += 1
                    if player_score == 2:
                        player_twos += 1
                    if player_score == 3:
                        player_threes += 1
                else:
                    player_score = 0

        # diagonal /
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.ROWS - (self.TO_WIN - 1)):
                if self.board[row][col] == 1 and self.board[row + 1][col + 1] == 1 and self.board[row + 2][col + 2] == 1:
                    ai_threes += 1
                elif self.board[row][col] == 1 and self.board[row + 1][col + 1] == 1:
                    ai_twos += 1
                if self.board[row][col] == 0 and self.board[row + 1][col + 1] == 0 and self.board[row + 2][col + 2] == 0:
                    player_threes += 1
                elif self.board[row][col] == 0 and self.board[row + 1][col + 1] == 0:
                    player_twos += 1

        # diagonal \
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.TO_WIN - 1, self.ROWS):
                if self.board[row][col] == 1 and self.board[row - 1][col + 1] == 1 and self.board[row - 2][col + 2] == 1:
                    ai_threes += 1
                if self.board[row][col] == 1 and self.board[row - 1][col + 1] == 1:
                    ai_twos += 1
                if self.board[row][col] == 0 and self.board[row - 1][col + 1] == 0 and self.board[row - 2][col + 2] == 0:
                    player_threes += 1
                if self.board[row][col] == 0 and self.board[row - 1][col + 1] == 0:
                    player_twos += 1

        return ((3 * ai_threes) + ai_twos) - ((3 * player_threes) + player_twos)


def minimax(game):
    game_state = GameState(game)
<<<<<<< HEAD
    result = max_value(game_state, 0, 5, -9999999, 99999999, 0)
=======
    result = max_value(game_state, 0, 5, -9999999, 99999999)
    print("RESULTS MINIMAX")
>>>>>>> aa2fb27674eac35940f4a80cfc705408d25e678b
    print(result)
    return result[0]


def max_value(game_state, num_moves, max_depth, alpha, beta,DANGERFACTOR):
    if game_state.is_win(1):
        return [None, 100]  # computer wins
    elif game_state.is_win(0):
        return [None, -100]  # player wins
    elif game_state.is_tie():
        return [None, 0]  # not sure what score for tie should be
    elif num_moves > max_depth:
        return [None, game_state.dangerous_good_h(DANGERFACTOR)]
    cur_max = -999999999
    move = None
    # print(game_state.board)
    # print(game_state.get_successors())
    for successor in game_state.get_successors():
        row = successor[0]
        col = successor[1]
        new_game_state = GameState(game_state)
        new_game_state.board[row][col] = 1  # computer move
        new_max = min_value(new_game_state, num_moves + 1, max_depth, alpha, beta, DANGERFACTOR)[1]
        if new_max >= cur_max:
            cur_max = new_max
            move = successor
        if cur_max > beta:
            return [move, cur_max]
        alpha = max(alpha, cur_max)
    return [move, cur_max]


def min_value(game_state, num_moves, max_depth, alpha, beta, DANGERFACTOR):
    if game_state.is_win(1):
        return [None, 100]  # computer wins
    elif game_state.is_win(0):
        return [None, -100]  # player wins
    elif game_state.is_tie():
        return [None, 0]  # not sure what score for tie should be
    elif num_moves > max_depth:
        return [None, game_state.dangerous_good_h(DANGERFACTOR)]
    cur_min = 999999999
    move = None
    for successor in game_state.get_successors():
        row = successor[0]
        col = successor[1]
        new_game_state = GameState(game_state)
        new_game_state.board[row][col] = 0  # player move
        new_min = max_value(new_game_state, num_moves + 1, max_depth, alpha, beta, DANGERFACTOR)[1]
        if new_min <= cur_min:
            cur_min = new_min
            move = successor
        if cur_min < alpha:
            return [move, cur_min]
        beta = min(beta, cur_min)
    return [move, cur_min]


def expectimax(game):
    game_state = GameState(game)
    result = e_max_value(game_state, 0, 4)
    print("RESULTS E MAX")
    print(result)
    return result[0]


def e_max_value(game_state, num_moves, max_depth):
    if game_state.is_win(1):
        return [None, 100]  # computer wins
    elif game_state.is_win(0):
        return [None, -100]  # player wins
    elif game_state.is_tie():
        return [None, 0]  # not sure what score for tie should be
    elif num_moves > max_depth:
        return [None, game_state.get_score()]
    cur_max = -999999999
    move = None
    # print(game_state.board)
    # print(game_state.get_successors())
    for successor in game_state.get_successors():
        row = successor[0]
        col = successor[1]
        new_game_state = GameState(game_state)
        new_game_state.board[row][col] = 1  # computer move
        new_max = e_min_value(new_game_state, num_moves + 1, max_depth)[1]
        if new_max >= cur_max:
            cur_max = new_max
            move = successor
    return [move, cur_max]


def e_min_value(game_state, num_moves, max_depth):
    if game_state.is_win(1):
        return [None, 100]  # computer wins
    elif game_state.is_win(0):
        return [None, -100]  # player wins
    elif game_state.is_tie():
        return [None, 0]  # not sure what score for tie should be
    elif num_moves > max_depth:
        return [None, game_state.get_score()]

    move = None
    total_value = 0
    successors = game_state.get_successors()
    for successor in successors:
        row = successor[0]
        col = successor[1]
        new_game_state = GameState(game_state)
        new_game_state.board[row][col] = 0  # player move
        value = e_max_value(new_game_state, num_moves + 1, max_depth)[1]
        total_value += value
    final_value = total_value/len(successors)
    return [move, final_value]
