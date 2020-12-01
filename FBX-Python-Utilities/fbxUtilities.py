import fbx, scandir,timeit, threading, os
from multiprocessing.pool import ThreadPool #FBX SDK code, however, is not guaranteed to be thread-safe https://download.autodesk.com/us/fbx/20112/FBX_SDK_HELP/index.html?url=WS1a9193826455f5ff-150b16da11960d83164-6bf0.htm,topicNumber=d0e1518
from ImportScene import DisplayMetaData
from FbxCommon import LoadScene, InitializeSdkObjects
from ProgressBar import ProgressBarUpdate
from FileSystemUtilities import GetListFilenamePath,GetListFromFolderOfExt,WriteToFile

def GetHierarchyListFromFBXFile(filePath):
    """Get a list of fbx file and its Hierarchy

    Args:
        filePath (str): os.path.isfile formatted str

    Raises:
        TypeError: expecting str filePath
        ValueError: expecting path formatted str

    Returns:
        list(): fbx file Hierarchy
    """
    if(isinstance(filePath,str)):
        if(os.path.isfile(filePath)):
            scene = GetSceneFromFBXFile(filePath)
            hierarchyList = GetSceneHierarchyAsList(scene)
            return hierarchyList
        else:
            raise ValueError("Expected a path formatted str. Got {}".format(filePath))
    else:
        raise TypeError("expected str for filePath got {}".format(type(filePath)))

def GetSceneFromFBXFile(filePath): #Ony for unitTesting
    """Returns an FBX Scene Object from the fbx file @ filePath

    Args:
        filePath (str): an os.path.isfile valid formatted string

    Raises:
        ValueError: if path is not a file formatted path
        TypeError: if filePath is not a str

    Returns:
        FbxScene: FbxScene Object loaded from SDK Manager @ filtPath
    """
    if(isinstance(filePath,str)):
        if(os.path.isfile(filePath)):
            # Prepare the FBX SDK.
            lSdkManager, lScene = InitializeSdkObjects()
            lResult = LoadScene(lSdkManager, lScene, filePath)
            if not lResult:
                print("\n\nAn error occurred while loading the scene...")
            else:
                return lScene # Once Scene Passes out of script cann't access node information
        else:
            raise ValueError("Expected a path formatted str. Got {}".format(filePath))
    else:
        raise TypeError("expected str for filePath got {}".format(type(filePath)))

def GetRootNodeFromFBXFile(filePath):
    """Get Root fbx.FbxNode Object from fbx file @ filePath 

    Args:
        filePath (str): an os.path.isfile valid formatted string

    Raises:
        ValueError: if filePath  not valid os.path.isfile formatted path
        TypeError: if filePath is not a str

    Returns:
        fbx.FbxNode: Root Node of Scene loaded from FBX File
    """
    if(isinstance(filePath,str)):
        if(os.path.isfile(filePath)):
            # Prepare the FBX SDK.
            lScene = GetSceneFromFBXFile(filePath)
            lRootNode = lScene.GetRootNode()
            return lRootNode
        else:
            raise ValueError("Expected a path formatted str. Got {}".format(filePath))
    else:
        raise TypeError("expected str for filePath got {}".format(type(filePath)))
    

def GetSceneHierarchyAsList(lScene):
    """Get fbx.FbxScene RootNode and sub-nodes names as str list

    Args:
        lScene (fbx.FbxScene): FBX Scene to get nodes from

    Raises:
        TypeError: lScene needs to be an fbx.FbxScene Object

    Returns:
        list(str): fbx.FbxNode name list
    """
    if(isinstance(lScene,fbx.FbxScene)):
        output_list = []

        lRootNode = lScene.GetRootNode()
        output_list = GetNodeHierarchyAsList(lRootNode, 0)
        return output_list
    else:
        raise TypeError("Expected lScene to be an fbx.FbxScene Object got {}".format(type(lScene)))

def GetNodeHierarchyAsList(pNode, pDepth):
    """Get Nodes name and sub nodes name as list

    Args:
        pNode (fbx.FbxNode): fbx.FbxNode to get name and parse for subNodes
        pDepth (int): current depth of node

    Raises:
        TypeError: Expecting fbx.FbxNode and int
        ValueError: Expecting a non-Negative value for pDepth

    Returns:
        list(str): Node and sub-nodes names list
    """
    if(isinstance(pNode,fbx.FbxNode) and isinstance(pDepth,int)):
        if(pDepth > -1):
            outputList = []
            outputList.append(pNode.GetName())
            for i in range(pNode.GetChildCount()):
                lowerNodeSet = GetNodeHierarchyAsList(pNode.GetChild(i), pDepth + 1)
                if(lowerNodeSet != None):
                    outputList.extend(lowerNodeSet)
            return outputList
        else:
            raise ValueError("pDepth needs to be a non-negative value. Got {}".format(pDepth))
    else:
        raise TypeError("Expected pNode to be an fbx.FbxNode Object and pDepth to be int. pNode = {} pDepth = {}".format(type(pNode),type(pDepth)))

def GetNodeHierarchyAsListByVisibility(pNode, pDepth, visibility):
    """Get Node name and sub-node names based on visibility

    Args:
        pNode (fbx.FbxNode): fbx.FbxNode to check visibility and return name
        pDepth (int): level within node
        visibility (float): 0 or 1 for on or off

    Raises:
        TypeError: Expecting fbx.FbxNode, int and float
        ValueError: Expecting visibility between 0-1 and pDepth > 0

    Returns:
        list(): list of node names and sub-node names
    """
    if(isinstance(pNode,fbx.FbxNode) and isinstance(pDepth,int) and isinstance(visibility,float)):
        if(visibility >= 0.0 and visibility <= 1.0 and pDepth >= 0):
            outputList = []
            if(pNode.Visibility.Get() == visibility):
                outputList.append(pNode.GetName())
            for i in range(pNode.GetChildCount()):
                lowerNodeSet = GetNodeHierarchyAsListByVisibility(pNode.GetChild(i), pDepth, visibility)
                if(lowerNodeSet != None):
                    outputList.extend(lowerNodeSet)
            return outputList
        else:
            raise ValueError("Expected visibility to be between 0-1 and pDepth >= 0. visibilty = {} and pDepth = {}".format(visibility,pDepth))
    else:
        raise TypeError("Expected fbx.FbxNode, int, float/int. Got {},{},{}".format(type(pNode),type(pDepth),type(visibility)))

def GenerateDictionaryFBXAndHierarchyFromFolder(directoryPath):
    """Iterate over files @ directoryPath and return Dict of filename:List(Fbx hierarchy)

    Args:
        directoryPath (string): An os.path.isdir valid formatted path to a direcotry with .fbx files

    Raises:
        TypeError: if the directoryPath != str
        ValueError: if directoryPath not a valid direcotry formatted path str

    Returns:
        dict(): fbx filename: List(File Hierarchy}
    """
    if(isinstance(directoryPath,str)):
        if(os.path.isdir(directoryPath)):
            outputDictionary = dict()
            count = 0
            totalFiles = len(os.listdir(directoryPath))
            ProgressBarUpdate(count,totalFiles,"Generating Dictionary from FBX's Hierarchy From Folder")
            for entry in scandir.scandir(directoryPath):
                if (entry.path.endswith(".fbx")):
                    fbxName = entry.name.replace(".fbx","")
                    outputDictionary[fbxName] = GetHierarchyListFromFBXFile(entry.path)
                count += 1
                ProgressBarUpdate(count,totalFiles,"Generating Dictionary from FBX's Hierarchy From Folder")
            return outputDictionary
        else:
            raise(ValueError("directoryPath needs to be directory formatted str. Got {}".format(directoryPath)))
    else:
        raise(TypeError("expecting a str for directoryPath got {}".format(type(directoryPath))))