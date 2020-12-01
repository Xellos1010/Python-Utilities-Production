import unittest
import fbx
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)
from fbxUtilities import GetHierarchyListFromFBXFile,GetSceneFromFBXFile, GetSceneHierarchyAsList, GetNodeHierarchyAsList, GetNodeHierarchyAsListByVisibility, GenerateDictionaryFBXAndHierarchyFromFolder, GetRootNodeFromFBXFile

class MainTests(unittest.TestCase):
    ##GetHierarchyListFromFBXFile##
    # Test Correct
    def testCorrectGetHierarchyListFromFBXFile(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        #Check that you return the test files full Hierarchy based on fbx_path
        self.failUnlessEqual(GetHierarchyListFromFBXFile(fbx_file_path),[u'RootNode',u'carParent', u'test1', u'pCube2', u'test2', u'pCube1'])
    
    ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetHierarchyListFromFBXFile(self):
        fbx_file_path = 1234
        with self.failUnlessRaises(TypeError): 
            GetHierarchyListFromFBXFile(fbx_file_path)
    ##
    #Value Test
    def testFailUnlessRaisesValueErrorGetHierarchyListFromFBXFile(self):
        fbx_file_path = 'visibility.fbx'
        with self.failUnlessRaises(ValueError): 
            GetHierarchyListFromFBXFile(fbx_file_path)
    ####
    ##GetSceneFromFBXFile##
    #Test Correct
    def testCorrectGetSceneFromFBXFile(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        self.failUnlessEqual(type(GetSceneFromFBXFile(fbx_file_path)),fbx.FbxScene)
    
    ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetSceneFromFBXFile(self):
        fbx_file_path = 1234
        with self.failUnlessRaises(TypeError): 
            GetSceneFromFBXFile(fbx_file_path)
    ##
    #Value Test
    def testFailUnlessRaisesValueErrorGetSceneFromFBXFile(self):
        fbx_file_path = 'visibility.fbx'
        with self.failUnlessRaises(ValueError): 
            GetSceneFromFBXFile(fbx_file_path)    
    ####
    ##GetRootNodeFromFBXFile##
    #Test Correct 
    def testCorrectGetRootNodeFromFBXFile(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        self.failUnlessEqual(type(GetRootNodeFromFBXFile(fbx_file_path)),fbx.FbxNode)

    ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetRootNodeFromFBXFile(self):
        fbx_file_path = 1234
        with self.failUnlessRaises(TypeError): 
            GetRootNodeFromFBXFile(fbx_file_path)
    ##
    #Value Test
    def testFailUnlessRaisesValueErrorGetRootNodeFromFBXFile(self):
        fbx_file_path = 'visibility.fbx'
        with self.failUnlessRaises(ValueError): 
            GetRootNodeFromFBXFile(fbx_file_path)

    ##GetSceneHierarchyAsList##
    #Test Correct 
    def testCorrectGetSceneHierarchyAsList(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        scene = GetSceneFromFBXFile(fbx_file_path)
        #Check return based on FBXScene
        self.failUnlessEqual(GetSceneHierarchyAsList(scene),[u'RootNode',u'carParent', u'test1', u'pCube2', u'test2', u'pCube1'])
    ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesGetSceneHierarchyAsList(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        node = GetRootNodeFromFBXFile(fbx_file_path)
        with self.failUnlessRaises(TypeError):
            GetSceneHierarchyAsList(node)
        
    ##GetNodeHierarchyAsList##
    #Test Correct
    def testCorrectGetNodeHierarchyAsList(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        node = GetRootNodeFromFBXFile(fbx_file_path)
        #Check return files based on Root Node
        self.failUnlessEqual(GetNodeHierarchyAsList(node,0),[u'RootNode',u'carParent', u'test1', u'pCube2', u'test2', u'pCube1'])
        #Check return of Child Node
        self.failUnlessEqual(GetNodeHierarchyAsList(node.GetChild(0),0),[u'carParent', u'test1', u'pCube2', u'test2', u'pCube1'])
    
    ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetHierarchyListFromFBXFile(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        try:
            scene = GetSceneFromFBXFile(fbx_file_path)
        except ValueError as e: #if visibilityTest.fbx does not exist
            raise(e)
        #Check that you return the test files full Hierarchy based on FBXScene
        with self.failUnlessRaises(TypeError):
            GetNodeHierarchyAsList(scene)
    ####
    ##GetNodeHierarchyAsListByVisibility##
    #Test Correct Get Visible by 1.0
    def testCorrectGetNodeHierarchyAsListByVisibility(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        node = GetRootNodeFromFBXFile(fbx_file_path)
        #Check that you return the test files Hierarchy based Visible = 1
        self.failUnlessEqual(GetNodeHierarchyAsListByVisibility(node,0,1.0),[u'RootNode', u'carParent', u'test1', u'pCube2', u'pCube1'])

    #Test Correct Get Visible by 0.0
    def testCorrectGetNodeHierarchyAsListByVisibilityOff(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        node = GetRootNodeFromFBXFile(fbx_file_path)
        #Check that you return the test files Hierarchy based on Visible = 0
        self.failUnlessEqual(GetNodeHierarchyAsListByVisibility(node,0,0.0),[u'test2'])

     ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetNodeHierarchyAsListByVisibility(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        try:
            scene = GetSceneFromFBXFile(fbx_file_path)
            lRootNode = scene.GetRootNode()
        except ValueError as e: #if visibilityTest.fbx does not exist
            raise(e)
        #Check that you return the test files full Hierarchy based on FBXScene
        with self.failUnlessRaises(TypeError):
            GetNodeHierarchyAsListByVisibility(scene,0,1.0) 

        with self.failUnlessRaises(TypeError):
            GetNodeHierarchyAsListByVisibility(lRootNode,0,1)

        with self.failUnlessRaises(TypeError):
            GetNodeHierarchyAsListByVisibility(lRootNode,'0',1.0)
    ##
    #Value Test
    def testFailUnlessRaisesValueErrorGetNodeHierarchyAsListByVisibility(self):
        fbx_file_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests','visibilityTest.fbx')
        try:
            scene = GetSceneFromFBXFile(fbx_file_path)
            lRootNode = scene.GetRootNode()
        except ValueError as e: #if visibilityTest.fbx does not exist
            raise(e)
        #Check that you return the test files full Hierarchy based on FBXScene
        with self.failUnlessRaises(ValueError):
            GetNodeHierarchyAsListByVisibility(lRootNode,-1,1.0) 

        with self.failUnlessRaises(ValueError):
            GetNodeHierarchyAsListByVisibility(lRootNode,0,-1.0)

        with self.failUnlessRaises(ValueError):
            GetNodeHierarchyAsListByVisibility(lRootNode,0,1.5)
    ##
    ##GenerateDictionaryFBXAndHierarchyFromFolder##
    #Test Correct
    def testCorrectGenerateDictionaryFBXAndHierarchyFromFolder(self):
        fbx_directory_path = os.path.join(os.getcwd(),'GarageAssemblyUtilities','GarageChecker','tests')
        self.failUnlessEqual(GenerateDictionaryFBXAndHierarchyFromFolder(fbx_directory_path),{'visibilityTest': [u'RootNode', u'carParent', u'test1', u'pCube2', u'test2', u'pCube1']})
     ##Raise Error Tests##
    #Type Test
    def testFailUnlessRaisesTypeErrorGetRootNodeFromFBXFile(self):
        fbx_file_path = 1234
        with self.failUnlessRaises(TypeError): 
            GenerateDictionaryFBXAndHierarchyFromFolder(fbx_file_path)
    ##
    #Value Test 
    def testFailUnlessRaisesValueErrorGetRootNodeFromFBXFile(self):
        fbx_file_path = 'visibility.fbx'
        with self.failUnlessRaises(ValueError): 
            GenerateDictionaryFBXAndHierarchyFromFolder(fbx_file_path)
    ####

if __name__ == "__main__":
    unittest.main()
