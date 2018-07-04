import unittest
from TicTacToe import TicTacToe

class EmptyTest(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(True)

class TicTacToeTests(unittest.TestCase):
    def constructor(self):
        game = TicTacToe()
    
    def setFieldTest(self):
        game = TicTacToe()
        game.setField(1,1,2)
        self.assertEquals(game.board,[[0,0,0],[0,5,0],[0,0,0]])

if __name__ == '__main__':
    unittest.main()
