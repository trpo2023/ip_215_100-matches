import unittest
from game import print_description, change_player, is_input_correct

class TestGame(unittest.TestCase):

    def test_print_description(self):
        # Тестирование вывода описания игры
        expected_output = "Из кучки, первоначально содержащей 100 спичек, два игрока поочередно берут по несколько спичек:\n"\
                          "не менее одной и не более десяти.\n"\
                          "Выигрывает тот, кто берет последнюю спичку.\n"\
                          "\nДля возврата в меню нажмите любую клавишу...\n"
        with self.assertRaises(SystemExit):
            with unittest.mock.patch('builtins.input', return_value=''):
                with unittest.mock.patch('builtins.print') as mock_print:
                    print_description()
                    mock_print.assert_called_with(expected_output)

    def test_change_player(self):
        # Тестирование функции смены игрока
        self.assertEqual(change_player(1), 2)
        self.assertEqual(change_player(2), 1)

    def test_is_input_correct(self):
        # Тестирование проверки корректности ввода
        self.assertFalse(is_input_correct(0))
        self.assertFalse(is_input_correct(11))
        self.assertTrue(is_input_correct(1))
        self.assertTrue(is_input_correct(5))
        self.assertTrue(is_input_correct(10))

if __name__ == '__main__':
    unittest.main()
