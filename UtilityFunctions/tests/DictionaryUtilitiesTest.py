import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)

from DictionaryUtilities import MergeDicts

class MainTests(unittest.TestCase):
    ##MergeDicts Tests##
    #Test Correct
    def testCorrect(self):
        dict1 = {'something':'value'}
        dict2 = {'something2':'value2'}
        self.failUnlessEqual(MergeDicts(dict1,dict2),{'something':'value','something2':'value2'})
    ##Raise Error Tests##
    #Type Error Test
    def testFailUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            MergeDicts(['something'],['something2'])
    ####

if __name__ == "__main__":
    unittest.main()
