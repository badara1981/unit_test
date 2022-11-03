import unittest

from division import division


class Testdivision(unittest.TestCase):
    
    def division(self):
        self.assertEqual(division(20, 2), 10)

if __name__ == '__main__':
    unittest.main()
