import borders
import unittest


class BordTests(unittest.TestCase):
    def test_inputNum(self):
        inputNum = 0
        self.assertFalse(borders.inputNum(inputNum))

        inputNum = 11
        self.assertFalse(borders.inputNum(inputNum))

        inputNum = 7
        self.assertTrue(borders.inputNum(inputNum))

        inputNum = 10
        self.assertTrue(borders.inputNum(inputNum))

    def test_inputNum2(self):
        inputNum = 5
        count = 4
        self.assertFalse(borders.inputNum2(inputNum, count))

        inputNum = 7
        count = 1
        self.assertFalse(borders.inputNum2(inputNum, count))

        inputNum = 3
        count = 6
        self.assertTrue(borders.inputNum2(inputNum, count))

        inputNum = 9
        count = 26
        self.assertTrue(borders.inputNum2(inputNum, count))

    def test_compNum(self):
        compNum = 9
        count = 4
        self.assertFalse(borders.pcNum(compNum, count))

        compNum = 7
        count = 6
        self.assertFalse(borders.pcNum(compNum, count))

        compNum = 3
        count = 6
        self.assertTrue(borders.pcNum(compNum, count))

        compNum = 7
        count = 15
        self.assertTrue(borders.pcNum(compNum, count))


if __name__ == "__main__":
    unittest.main()
