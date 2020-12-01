import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)

from UserInputUtilities import GetUserInputDirectory,GetUserInputFile

class MainTests(unittest.TestCase):
    ##GetUserInputDirectory Tests##
    #Test Correct
    def testCorrectGetUserInputDirectory(self):
        test_cwd = os.path.join(os.getcwd(),'TestFileGeneration')
        #Generate folder and file to test for then delete
        if(not os.path.isdir(test_cwd)):
            try:
                os.makedirs(test_cwd)
            except OSError:
                print("Creation of the directory {} has failed".format(test_cwd))
        self.failUnlessEqual(GetUserInputDirectory("Input Test Directory: ",test_cwd),test_cwd)
        os.rmdir(test_cwd)
    ##Raise Error Tests##
    #Type Error Test
    def testFailUnlessRaisesGetUserInputDirectory(self):
        with self.failUnlessRaises(TypeError): 
            GetUserInputDirectory(1234)
    ####
    ##GetUserInputFile Tests##
    #Test Correct
    def testCorrectFileGetUserInputFile(self):
        test_cwd = os.path.join(os.getcwd(),'TestFileGeneration')
        test_cwd_file = os.path.join(test_cwd,'testText.txt')
        if(not os.path.isdir(test_cwd)):
            try:
                os.makedirs(test_cwd)
            except OSError:
                print("Creation of the directory {} has failed".format(test_cwd))
            f = open(test_cwd_file,"w+")
            f.close()
        self.failUnlessEqual(GetUserInputFile("Input Test file path: ",test_cwd_file),test_cwd_file)
        os.remove(test_cwd_file)
        os.rmdir(test_cwd)
    ##Raise Error Tests##
    #Type Error Test
    def testFailUnlessRaisesGetUserInputFile(self):
        with self.failUnlessRaises(TypeError): 
            GetUserInputFile(1234)
    ####
if __name__ == "__main__":
    unittest.main()
