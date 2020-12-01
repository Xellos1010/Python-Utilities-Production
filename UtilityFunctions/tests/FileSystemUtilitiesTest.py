import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)

from FileSystemUtilities import WriteToFile,WriteArrayToFileWithDelimiter,GetListFromFolderOfExt,BuildDictFromFolderWithExt,RemoveFolderAtPath,RemoveFileAtPath, CopyFileFromTo

class MainTests(unittest.TestCase):

    ##WriteToFile Tests##
    # Correct call statement
    def testCorrectWriteToFile(self):
        dict2 = {'something2':'value2'}
        self.failUnlessEqual(WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2),None)

    ##Exception Tests##
    def testFailWriteToFileUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            WriteToFile(132,['something2'])
        with self.failUnlessRaises(ValueError): 
            WriteToFile('fail.txt',['something2'])
    ####
    ##WriteArrayToFileWithDelimiter Tests##
    # Correct call statement
    def testCorrectWriteArrayToFileWithDelimiter(self):
        list = ['something2','value2']
        self.failUnlessEqual(WriteArrayToFileWithDelimiter(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),list,','),'something2,value2')

    ##Exception Tests##
    def testFailWriteArrayToFileWithDelimiterUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            WriteArrayToFileWithDelimiter(132,['something2'],',')
        with self.failUnlessRaises(ValueError): 
            WriteArrayToFileWithDelimiter('fail.txt',['something2'],',')
    ####
    ##GetListFromFolderOfExt Tests##
    # Correct call statement
    def testCorrectGetListFromFolderOfExt(self):
        dict2 = {'something2':'value2'}
        WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2)

        self.failUnlessEqual(GetListFromFolderOfExt(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),'.txt'),['FileSystemTest'])

    ##Exception Tests##
    def testFailGetListFromFolderOfExtUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            GetListFromFolderOfExt(132,'.txt')
        with self.failUnlessRaises(TypeError): 
            GetListFromFolderOfExt(os.path.join(os.getcwd(),'FileUtilityTestFolder'),['.txt'])
        with self.failUnlessRaises(ValueError): 
            GetListFromFolderOfExt('failFilePath.txt','.txt')
    ####
    ##BuildDictFromFolderWithExt Tests##
    # Correct call statement
    def testCorrectBuildDictFromFolderWithExt(self):
        dict2 = {'something2':'value2'}
        WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2)
        self.failUnlessEqual(BuildDictFromFolderWithExt(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),'.txt',False),{'FileSystemTest':[os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt')]})

    #Exception Tests
    def testFailBuildDictFromFolderWithExtUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            BuildDictFromFolderWithExt(132,['something2'],',')
        with self.failUnlessRaises(ValueError): 
            BuildDictFromFolderWithExt('fail.txt',',')
    ####
    ##RemoveFolderAtPath Tests##
    # Correct call statement
    def testCorrectRemoveFolderAtPath(self):
        dict2 = {'something2':'value2'}
        WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2)
        self.failUnlessEqual(RemoveFolderAtPath(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),True),None)

    #Exception Tests
    def testFailRemoveFolderAtPathUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            RemoveFolderAtPath(132,True)
        with self.failUnlessRaises(TypeError): 
            RemoveFolderAtPath(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),'True')
        with self.failUnlessRaises(ValueError): 
            RemoveFolderAtPath('fail.txt',True)
        #with self.failUnlessRaises(OSError): #TODO how to raise OS Error? 
        #    RemoveFolderAtPath('fail.txt',',')
    ####
    ##RemoveFileAtPath Tests##
    # Correct call statement
    def testCorrectRemoveFileAtPath(self):
        dict2 = {'something2':'value2'}
        WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2)
        self.failUnlessEqual(RemoveFileAtPath(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt')),None)

    #Exception Tests
    def testFailRemoveFileAtPathUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            RemoveFileAtPath(132,True)
        with self.failUnlessRaises(TypeError): 
            RemoveFileAtPath(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),'True')
        with self.failUnlessRaises(ValueError): 
            RemoveFileAtPath('fail.txt')
        #with self.failUnlessRaises(OSError): #TODO how to raise OS Error? 
        #    RemoveFileAtPath('fail.txt')
    ####
    ##CopyFileFromTo Tests##
    # Correct call statement
    def testCorrectCopyFileFromTo(self):
        dict2 = {'something2':'value2'}
        WriteToFile(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),dict2)
        self.failUnlessEqual(CopyFileFromTo(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'),os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolderCopyToTest','FileSystemTest.txt')),None)

    #Exception Tests
    def testFailCopyFileFromToUnlessRaises(self):
        with self.failUnlessRaises(TypeError): 
            CopyFileFromTo(132,os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'))
        with self.failUnlessRaises(TypeError): 
            CopyFileFromTo(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'))
        with self.failUnlessRaises(ValueError): 
            CopyFileFromTo(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'))
        with self.failUnlessRaises(ValueError): 
            CopyFileFromTo(os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder'),os.path.join(os.getcwd(),'__tests__','FileUtilityTestFolder','FileSystemTest.txt'))
        #with self.failUnlessRaises(OSError): #TODO how to raise OS Error? 
        #    RemoveFileAtPath('fail.txt')
    ####

if __name__ == "__main__":
    unittest.main()
