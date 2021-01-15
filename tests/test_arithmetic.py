import unittest
import os


class TestArithmetic(unittest.TestCase):

    def test_arithmetic(self):
        IMP_PATH = "../testy2020/arithmetic.imp"
        os.system("kompilator.py {} testyWyniki/arithmetic.mr".format(IMP_PATH))


if __name__ == '__main__':
    unittest.main()
