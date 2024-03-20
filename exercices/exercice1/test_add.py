import unittest
from add import add


class testFunctionADD(unittest.TestCase):
    def test_add_positive_numbers(self):
        '''TESTER L'ADDITION DE NOMBRES POSITIFS'''
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        '''TESTER L'ADDITION DE NOMBRES NEGATIFS'''
        self.assertEqual(add(-5, -3), -8)

    def test_add_positive_and_negative_numbers(self):
        '''TESTER L'ADDITION DE NOMBRES POSITIFS ET NEGATIFS'''
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)

    def test_add_zero(self):
        '''TESTER L'ADDITION DU NOMBRE 0'''
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-5, 0), -5)


if __name__ == '__main__':
    unittest.main()
