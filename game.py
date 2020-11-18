class ConnectFour:
    
    def __init__(self, rows=5, cols=6, to_win=4):
        self.turn = 0
        self.ROWS = rows
        self.COLS = cols
        self.PLAYERS = 2
        self.TO_WIN = to_win
        self.winner = None
        self.board = None
        self.reset()
        # self.test()

    def reset(self):
        self.board = [[None for i in range(self.COLS)] for j in range(self.ROWS)] 
        self.turn = 0
        self.winner = None
        # print(self.board) 
    
    def make_board(self, board):
        self.board = board
    

    def ai_make_move(self):
        return None

    def make_move(self, col):
        row = self.next_valid(col)
        if row is not None:
            self.board[row][col] = self.turn
            # print(self)
            self.is_win(col, row, self.turn)
            if self.winner == 2:
                print(f'It was a tie')
            elif self.is_win(col, row, self.turn):
                print(f'Player {self.turn + 1} won!')
                return
            else: 
                self.turn = (self.turn + 1) % self.PLAYERS
                return row
        return None

    def get(self, col, row):
        return self.board[col][row]

    def is_win(self, col, row, player):
        #vertical
        c = 0
        for i in range(row, min(self.ROWS, row + self.TO_WIN)):
            if self.board[i][col] != player:
                break
            c += 1
            if c == self.TO_WIN:
                self.winner = player
                return True

        # horizontal
        c = 0
        for i in range(min(0, col-self.TO_WIN), min(col+self.TO_WIN, self.COLS)):
            if self.board[row][i] == player:
                c += 1
                if c == self.TO_WIN:
                    self.winner = player
                    return True
            else:
                c = 0

        # # diagonal /  TODO: TEST
        # c = 0
        # for row in range(max(0, row - self.TO_WIN), min(self.ROWS-1, row + self.TO_WIN)):
        #     for col in range(min(self.COLS-1, col + self.TO_WIN), max(0, col - self.TO_WIN), -1):
        #         # print(max(0, row - self.TO_WIN), min(self.ROWS, row + self.TO_WIN))
        #         # print(min(self.COLS, col + self.TO_WIN), max(0, col - self.TO_WIN), -1)
        #         # print(row, col)
        #         if self.board[row][col] == player:
        #             c += 1
        #             # print("Count", c, row, col)
        #             if c == self.TO_WIN:
        #                 self.winner = player
        #                 return True
        #         else:
        #             c = 0

        # # diagonal \  TODO: TEST
        # for row in range(min(0, row - self.TO_WIN), min(self.ROWS-1, row + self.TO_WIN)):
        #     for col in range(min(0, col - self.TO_WIN), min(self.COLS-1, col + self.TO_WIN), -1):
        #         if self.board[row][col] == player:
        #             c += 1
        #             if c == self.TO_WIN:
        #                 self.winner = player
        #                 return True
        #             else:
        #                 c = 0
        
        # positive diagonal
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.ROWS - (self.TO_WIN - 1)):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player and self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
                    self.winner = player
                    return True
                else:
                    c = 0

        # negative diagonal
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.TO_WIN - 1, self.ROWS):
                if self.board[row][col] == player and self.board[row - 1][col + 1] == player and self.board[row - 2][col + 2] == player and self.board[row - 3][col + 3] == player:
                    self.winner = player
                    return True
                else:
                    c = 0
    
        if self.is_tie():
            self.winner = 2
            return True

    def is_tie(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j] is None:
                    return False
        return True

    def next_valid(self, col):
        if self.board[0][col] is None:
            for row in range(self.ROWS-1, -1, -1):
                if self.board[row][col] is None:
                    return row
        return None
    
    def __str__(self):
        s = ""
        for row in range(self.ROWS):
            for col in range(self.COLS):
                s += (str(self.board[row][col]) + " ")
            s += "\n"
        return s


# game = ConnectFour()
# game.make_board(
#     [
#         [None,None,None,None,1,None],
#         [None,None,None,1,None,None],
#         [None,None,1,None,None,None],
#         [None,1,None,None,None,None],
#         [1,None,None,None,None,None]
#     ]
# )
# print((game))