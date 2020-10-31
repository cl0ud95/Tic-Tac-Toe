from Packages.Player import Player
from Packages.GameBoard import GameBoard
import unittest

class TestBoard(unittest.TestCase):
    """Tests the GameBoard class"""

    fake_board = GameBoard(5)

    def test_board_size(self):
        self.assertEqual(self.fake_board.max_box, 25)
    
    def test_board_matrix(self):
        self.assertEqual(self.fake_board.matrix,
            [[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]])             

    def test_draw_game(self):
        self.fake_board.turn_number = 25
        self.assertEqual(self.fake_board.stop_game(2, 2, 'Test Player'),
            'All boxes have been filled, the game ends in a draw')

    def test_win_game(self):
        self.fake_board.turn_number = 6
        fake_matrix = [['X',2,3,4,5],
                       [6,'X',8,9,10],
                       [11,12,'X',14,15],
                       [16,17,'O','O',20],
                       [21,'O',23,24,25]]

        self.fake_board.matrix = fake_matrix
        self.assertEqual(self.fake_board.stop_game(0, 0, 'Test Player'),
            'Congratulations Test Player! You have won!')

class TestPlayer(unittest.TestCase):
    """Tests the Player class"""

    fake_player = Player('Tester', 'X', 25)
    fake_matrix = [[1,2,3,4,5],
                    [6,'X',8,9,10],
                    [11,12,'X',14,15],
                    [16,17,'O','O',20],
                    [21,'O',23,24,25]]
    successful_matrix = [['X',2,3,4,5],
                         [6,'X',8,9,10],
                         [11,12,'X',14,15],
                         [16,17,'O','O',20],
                         [21,'O',23,24,25]]

    def test_box_out_of_bounds(self):
        self.assertEqual(self.fake_player.play(self.fake_matrix, 26, 6), 1)

    def test_box_already_filled(self):
        self.assertEqual(self.fake_player.play(self.fake_matrix, 7, 6), 2)
    
    def test_successful_play(self):
        self.assertEqual(self.fake_player.play(self.fake_matrix, 1, 6),
            [self.successful_matrix, 0, 0, 7])
                       
if __name__ == '__main__': 
    unittest.main()