import unittest

from multiplication import multiplication


class Testdivision(unittest.TestCase):
    
    def division(self):
        self.assertEqual(multiplication(20, 2), 40)

if __name__ == '__main__':
    unittest.main()
