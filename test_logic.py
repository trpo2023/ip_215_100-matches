import logic
import unittest


class LogicTests(unittest.TestCase):
    def test_check_inputNum(self):
        inputNum = 0
        self.assertFalse(logic.inputNum(inputNum))

        inputNum = 11
        self.assertFalse(logic.inputNum(inputNum))

        inputNum = 7
        self.assertTrue(logic.inputNum(inputNum))

        inputNum = 10
        self.assertTrue(logic.inputNum(inputNum))

    def test_check_inputNum2(self):
        inputNum = 5
        count = 4
        self.assertFalse(logic.inputNum2(inputNum, count))

        inputNum = 7
        count = 1
        self.assertFalse(logic.inputNum2(inputNum, count))

        inputNum = 3
        count = 6
        self.assertTrue(logic.inputNum2(inputNum, count))

        inputNum = 9
        count = 26
        self.assertTrue(logic.inputNum2(inputNum, count))

    def test_check_compNum(self):
        compNum = 9
        count = 4
        self.assertFalse(logic.pcNum(compNum, count))

        compNum = 7
        count = 6
        self.assertFalse(logic.pcNum(compNum, count))

        compNum = 3
        count = 6
        self.assertTrue(logic.pcNum(compNum, count))

        compNum = 7
        count = 15
        self.assertTrue(logic.pcNum(compNum, count))


if __name__ == "__main__":
    unittest.main()
