import unittest

from substraction import substraction


class Testsubstraction(unittest.TestCase):
    
    def substraction(self):
        self.assertEqual(substraction(20, 10), 10)

if __name__ == '__main__':
    unittest.main()
