import unittest
from unittest.mock import patch
import game

class GameTestCase(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_print_description(self, mock_input):
        with patch('builtins.print') as mock_print:
            game.print_description()
            mock_print.assert_called_with("Из кучки, первоначально содержащей 100 спичек, два игрока поочередно берут по несколько спичек:")
            mock_print.assert_called_with("не менее одной и не более десяти.")
            mock_print.assert_called_with("Выигрывает тот, кто берет последнюю спичку.")
            mock_input.assert_called_once()
            
    def test_change_player(self):
        player_number = 1
        self.assertEqual(game.change_player(player_number), 2)
        
        player_number = 2
        self.assertEqual(game.change_player(player_number), 1)
        
    def test_is_input_correct(self):
        self.assertFalse(game.is_input_correct(0))
        self.assertTrue(game.is_input_correct(1))
        self.assertTrue(game.is_input_correct(5))
        self.assertTrue(game.is_input_correct(10))
        self.assertFalse(game.is_input_correct(11))
        
    @patch('builtins.input', side_effect=['5', '8', '2', '12', '3'])
    def test_play_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            game.play_game()
            mock_print.assert_called_with("Начальное количество спичек:", 100)
            mock_print.assert_called_with("Игрок", 1, "выбирает спички:")
            mock_print.assert_called_with("Количество оставшихся спичек:", 95)
            mock_print.assert_called_with("Игрок", 2, "выбирает спички:")
            mock_print.assert_called_with("Количество оставшихся спичек:", 87)
            mock_print.assert_called_with("Необходимо выбрать количество спичек в диапазоне от 1 до 10")
            mock_input.assert_called_with()
            
if __name__ == '__main__':
    unittest.main()

