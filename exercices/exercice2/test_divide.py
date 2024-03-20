import unittest
from divide import divide


class testFunctionDIVIDE(unittest.TestCase):
    def test_divide_normal(self):
        '''TESTER LA DIVISION PAR NOMBRE AUTRE QUE 0'''
        self.assertAlmostEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(-10, 2), -5)
        self.assertAlmostEqual(divide(10, -2), -5)
        self.assertAlmostEqual(divide(-10, -2), 5)

    def test_divide_by_zero(self):
        '''TESTER LA DIVISION PAR 0'''
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
