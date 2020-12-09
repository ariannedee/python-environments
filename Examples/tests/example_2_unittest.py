import unittest

from rock_paper_scissors_buggy import determine_winner, game_over, YOU, COMP


class TestRPSGame(unittest.TestCase):
    def test_determine_winner(self):
        self.assertEqual(determine_winner('r', 'r'), None)
        self.assertEqual(determine_winner('r', 'p'), COMP)
        self.assertEqual(determine_winner('r', 's'), YOU)
        self.assertEqual(determine_winner('p', 'r'), YOU)
        self.assertEqual(determine_winner('p', 'p'), None)
        self.assertEqual(determine_winner('p', 's'), COMP)
        self.assertEqual(determine_winner('s', 'r'), COMP)
        self.assertEqual(determine_winner('s', 'p'), YOU)
        self.assertEqual(determine_winner('s', 's'), None)

    def test_game_over(self):
        self.assertEqual(game_over(3, [0, 0]), None)
        self.assertEqual(game_over(3, [1, 1]), None)
        self.assertEqual(game_over(3, [2, 1]), YOU)
        self.assertEqual(game_over(3, [1, 2]), COMP)
        self.assertEqual(game_over(5, [2, 2]), None)
        self.assertEqual(game_over(5, [3, 0]), YOU)
        self.assertEqual(game_over(5, [1, 3]), COMP)


if __name__ == '__main__':
    unittest.main()
