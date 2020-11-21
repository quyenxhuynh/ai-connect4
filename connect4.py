class ConnectFour:
    def __init__(self, rows=5, cols=6, to_win=4):
        self.turn = 1
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
        self.turn = 1
        self.winner = None
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

    def ai_make_move(self):
        return None

    def make_move(self, col):
        row = self.next_valid(col)
        if row is not None:
            self.board[row][col] = self.turn
            win = self.is_win(col, row, self.turn)
            print(self)
            if win:
                print(f'Player {self.turn} won!')
                return
            elif self.is_tie():
                print(f'It was a tie.')
            else: 
                self.turn = (self.turn + 1) % self.PLAYERS
                return row
        return None

    def get(self, col, row):
        return self.board[col][row]

    def is_win(self, col, row, player):
        c = 0
        for i in range(row, min(self.ROWS, row + self.TO_WIN)):
            if self.board[i][col] != player:
                break
            c += 1
            if c == self.TO_WIN:
                self.winner = player
                print("vertical")
                return True

        # horizontal
        for row in range(self.ROWS):
            c = 0
            for col in range(self.COLS):
                if self.board[row][col] == player:
                    c += 1
                    if c == self.TO_WIN:
                        self.winner = player
                        print("horizontal")
                        return True
                else:
                    c = 0
        # c = 0
        # for i in range(min(0, col-self.TO_WIN), min(col+self.TO_WIN, self.COLS)):
        #     if self.board[row][i] == player:
        #         c += 1
        #         if c == self.TO_WIN:
        #             self.winner = player
        #             print("horizontal")
        #
        #             return True
        #     else:
        #         c = 0

        # positive diagonal
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.ROWS - (self.TO_WIN - 1)):
                if self.board[row][col] == player and self.board[row + 1][col + 1] == player and self.board[row + 2][col + 2] == player and self.board[row + 3][col + 3] == player:
                    self.winner = player
                    print("positive diagonal")

                    return True
                else:
                    c = 0

        # negative diagonal
        for col in range(self.COLS - (self.TO_WIN - 1)):
            for row in range(self.TO_WIN - 1, self.ROWS):
                if self.board[row][col] == player and self.board[row - 1][col + 1] == player and self.board[row - 2][col + 2] == player and self.board[row - 3][col + 3] == player:
                    self.winner = player
                    print("negative diagonal")

                    return True
                else:
                    c = 0
        
    def is_tie(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j] is None:
                    return False
        self.winner = 2
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
                t = str(self.board[row][col])
                if t == "None":
                    s += "x "
                else:
                    s += (t + " ")
            s += "\n"
        return s