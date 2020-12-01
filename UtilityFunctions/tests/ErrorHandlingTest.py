import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)

from ErrorHandling import LogError

class MainTests(unittest.TestCase):

    def testCorrect(self):
        self.failUnlessEqual(LogError('Something is Wrong'),None)

    #Type Error Test
    def testFailUnlessRaises(self):
        self.failUnlessRaises(TypeError, LogError, 1346 )  

if __name__ == "__main__":
    unittest.main()
