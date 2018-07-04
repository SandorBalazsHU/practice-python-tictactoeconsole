class TicTacToe:
    'A 3x3-as amőba jtékot megvalóstó osztly.'

    #A jtéktáblát reprezentáló lista 0 - üres mező / 1 - első jtékos / 2 - msodik jtékos
    board = []

    def __init__(self):
        #A játéktáblát egy 3x3-as mtrixal implementljuk
        self.board = [ [0] * 3 ] * 3

    def setField(x,y,value):
        self.board[x,y] = value

    def getFreeFields():
        count = 0
        for i in board:
            if board[i] != 0: count += 1
        return count

    def _debugPrint():
        print(*self.board)

class CLIInterface:
    'A konzolos felhasznlói felület megvalóstsa.'

    def drawBoard(board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

game = TicTacToe()
game.setField(1,1,5)