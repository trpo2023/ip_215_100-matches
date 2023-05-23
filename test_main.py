from main import *
import unittest
class WrongInputException(Exception):
    pass
class MyTestCase(unittest.TestCase):
    def test_something(self):
        def digit_check():
            try:
                lenght = int(input('Enter the number:\n'))
                return lenght
            except ValueError:
                print('Please, enter the number\n')
                return digit_check()

        a = digit_check()
        print(a)

if __name__ == '__main__':
    unittest.main()
