class TicTacToe():
    def __init__(self, n = 3):
        self.size = n
        self.board = [[None for i in range(self.size)] for i in range(self.size)]
        self.turn = 0
        # -2 Default    -1 'O'    0 'Draw'    1 'X'
        self.victory = -2
        self.row = [[0,0] for i in range(self.size)]
        self.col = [[0,0] for i in range(self.size)]
        self.diag = [0,0]
        self.odiag = [0,0]
    def get_side(self):
        if self.turn % 2 == 0:
            return 'O'
        return 'X'

    def move(self, row, col):
        side = self.get_side()
        self.board[row][col] = side
        self.check_win(side, row, col)
        self.turn += 1

    def check_win(self, side, x, y):
        if side == 'O': side_num = 0
        else: side_num = 1

        self.row[x][side_num] += 1
        self.col[y][side_num] += 1
        if x==y:
            self.diag[side_num] += 1
        if x == self.size - y - 1:
            self.odiag[side_num] += 1

        if self.row[x][side_num] == self.size or self.col[y][side_num] == self.size or self.diag[side_num] == self.size or self.odiag[side_num] == self.size:
            if side_num == 0: self.victory = -1
            else: self.victory = 1
        elif self.turn == self.size * self.size - 1:
            self.victory = 0
