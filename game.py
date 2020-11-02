class ConnectFour:
    
    def __init__(self, rows=5, cols=6, to_win=4):
        self.turn = 0
        self.ROWS = rows
        self.COLS = cols
        self.PLAYERS = 2
        self.TO_WIN = to_win
        self.winner = None
        self.reset()
        # self.test()

    def reset(self):
        self.board = [[None for i in range(self.COLS)] for j in range(self.ROWS)] 
        self.turn = 0
        # print(self.board) 
    
    def make_board(self, board):
        self.board = board
    
    def test(self):
        self.board = [
            [0, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11], 
            [12, 13, 14, 15, 16, 17],
            [17, 18, 19, 20, 21, 22],
            [22, 23, 24, 25, 26, 27]
        ]
        print(self.board)

    def make_move(self, col):
        row = self.next_valid(col)
        if row is not None:
            self.board[row][col] = self.turn
            if (self.is_win(col, row, self.turn)):
                print(f'Player {self.turn} won!')
                self.reset()
                return
            else: 
                self.turn = (self.turn + 1) % self.PLAYERS
                return row
        return None

    def get(self, col, row):
        return self.board[col][row]

    def is_win(self, col, row, player):

        # N = len(self.board)
        # initial_val = [0]*N
        # rows = {
        #
        #     'Blue': initial_val,
        #     'Red': initial_val
        # }
        #
        # cols = {
        #     'Blue': initial_val,
        #     'Red': initial_val
        # }
        #
        # pos_diag = {
        #     'Blue': 0,
        #     'Red': 0
        # }
        #
        # neg_diag = {
        #     'Blue': 0,
        #     'Red': 0
        # }
        #
        # if row == col:
        #     pos_diag[player] += 1
        #     if pos_diag[player] == N:
        #         return player
        #
        # if row == N - col:
        #     neg_diag[player] += 1
        #     if neg_diag[player] == N:
        #         return [player]
        #
        # rows[player][row] += 1
        # cols[player][col] += 1
        #
        # if rows[player][row] or cols[player][col] == N:
        #     return player

        # vertical
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

        # diagonal /  TODO: TEST
        c = 0
        for row in range(max(0, row - self.TO_WIN), min(self.ROWS-1, row + self.TO_WIN)):
            for col in range(min(self.COLS-1, col + self.TO_WIN), max(0, col - self.TO_WIN), -1):
                # print(max(0, row - self.TO_WIN), min(self.ROWS, row + self.TO_WIN))
                # print(min(self.COLS, col + self.TO_WIN), max(0, col - self.TO_WIN), -1)
                # print(row, col)
                if self.board[row][col] == player:
                    c += 1
                    print("Count", c, row, col)
                    if c == self.TO_WIN:
                        self.winner = player
                        return True
                else:
                    c = 0

        # diagonal \  TODO: TEST
        for row in range(min(0, row - self.TO_WIN), min(self.ROWS-1, row + self.TO_WIN)):
            for col in range(min(0, col - self.TO_WIN), min(self.COLS-1, col + self.TO_WIN), -1):
                if self.board[row][col] == player:
                    c += 1
                    if c == self.TO_WIN:
                        self.winner = player
                        return True
                    else:
                        c = 0


    def next_valid(self, col):
        if self.board[0][col] is None:
            for row in range(self.ROWS-1, 0, -1):
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


game = ConnectFour()
game.make_board(
    [
        [None,None,None,None,1,None], 
        [None,None,None,1,None,None], 
        [None,None,1,None,None,None], 
        [None,1,None,None,None,None], 
        [1,None,None,None,None,None]
    ]
)

# print(game)