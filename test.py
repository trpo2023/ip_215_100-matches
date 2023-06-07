import unittest
from game import *


class GameTestCase(unittest.TestCase):
    def test_change_player(self):
        player = 1
        expected = 2
        change_player(player)
        self.assertEqual(expected, player)

        player = 2
        expected = 1
        change_player(player)
        self.assertEqual(expected, player)

    def test_is_input_correct(self):
        diff = 100
        real = is_input_correct(diff)
        self.assertFalse(real)

        diff = 0
        real = is_input_correct(diff)
        self.assertFalse(real)

        diff = 1
        real = is_input_correct(diff)
        self.assertTrue(real)

        diff = 5
        real = is_input_correct(diff)
        self.assertTrue(real)

        diff = 10
        real = is_input_correct(diff)
        self.assertTrue(real)


if __name__ == '__main__':
    unittest.main()
