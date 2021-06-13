from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from tictactoeclass import TicTacToe

class MenuWindow(QMainWindow):
    def __init__(self):
        super(MenuWindow,self).__init__()
        self.initUI()
        self.show()
        self.boardwin = None
    def button_clicked(self, choice):
        if choice == 1:
            self.boardwin = BoardWindow()
        elif choice == 0:
            if self.boardwin != None:
                self.boardwin.close()
            self.close()

    def initUI(self):
        self.setGeometry(500, 200, 400, 170)
        self.setWindowTitle("Tic Tac Toe")

        # self.score = [QtWidgets.QLabel('a',self) for i in range(3)]
        # self.score[0].setText('O: 0')
        # self.score[1].setText('X: 0')
        # self.score[2].setText('Draw: 0')        
        # self.score[0].setGeometry(50,10,30,30)
        # self.score[1].setGeometry(170,10,30,30)
        # self.score[2].setGeometry(290,10,30,30)

        self.single = QtWidgets.QPushButton(self)
        self.single.setText("Single")
        self.single.setGeometry(30, 50, 100, 100)
        self.single.clicked.connect(lambda: self.button_clicked(1))

        self.multi = QtWidgets.QPushButton(self)
        self.multi.setText("Online")
        self.multi.setGeometry(150, 50, 100, 100)
        self.multi.clicked.connect(lambda: self.button_clicked(2))

        self.ex = QtWidgets.QPushButton(self)
        self.ex.setText("Exit")
        self.ex.setGeometry(270, 50, 100, 100)
        self.ex.clicked.connect(lambda: self.button_clicked(0))

class BoardWindow(QMainWindow):
    def __init__(self):
        super(BoardWindow,self).__init__()
        self.ttt = TicTacToe()
        self.initUI()
        self.show()

    def button_clicked(self, row, col):
        if self.ttt.turn % 2 == 0:
            self.board[row][col].setText("O")
        else:
            self.board[row][col].setText("X")
        self.board[row][col].setFont(QtGui.QFont('Times',70))

        self.ttt.move(row,col)
        self.check_win_noti()
        self.board[row][col].disconnect() 

    def check_win_noti(self):
        noti = QMessageBox()
        end = False
        if self.ttt.victory == -1:
            noti.about(self,'Noti','O wins.')
            end = True
        elif self.ttt.victory == 1:
            noti.about(self,'Noti','X wins.')
            end = True
        elif self.ttt.victory == 0:
            noti.about(self,'Noti','Draw.')
            end = True
        if end == True:
            self.close()

    def init_cell_board(self):
        self.board = [[QtWidgets.QPushButton(self) for i in range(self.ttt.size)] for j in range(self.ttt.size)]
        for i in range(self.ttt.size):
            for j in range(self.ttt.size):
                self.board[i][j].setGeometry(j*100, i*100, 100, 100)
                self.board[i][j].clicked.connect((lambda temp, i = i, j = j: self.button_clicked(i,j)))
        
    def initUI(self):
        board_size = self.ttt.size * 100
        self.setGeometry(500, 200, board_size, board_size)
        self.setWindowTitle("Tic Tac Toe")
        self.init_cell_board()

    # def update(self):
    #     self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    menu = MenuWindow()
    sys.exit(app.exec_())

window()