"""
Created on 5.3.2017

@author: pkogler
"""
from bruch.Bruch import *
import unittest


class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass

    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    def testminus_erweitert(self):
        self.b = (self.b2 - self.b3)-self.b
        assert(Bruch(-2)== self.b)

    def testdivzero_erweitert(self):
        with self.assertRaises(ZeroDivisionError) as cm:
            self.b / 0

    def testinvert_erweitert(self):
        self.b.__invert__()
        assert(self.b == Bruch(3,2))

    def testTuple_erweitert(self):
        z, n = Bruch(3, 4)
        assert(z == 3 and n == 4)

    def testTuple3_Error_erweitert(self):
        b3 = list(self.b2)
        self.assertRaises(IndexError, self.tryIndex, b3, 3)

    @staticmethod
    def tryIndex(obj, index):
        return obj[index]

if __name__ == "__main__":
    unittest.main()
