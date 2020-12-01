import json, os, scandir, csv
from shutil import copy2

def WriteToFile(filename, objectToWrite):
    """Write a jsonObject to File

    Args:
        filename (str): valid path formatted str
        objectToWrite (dict, list, str): Dictionary of data to write

    Raises:
        IOError: If can't write to file then raises
        OSError: If can't make dir to file to write
        TypeError: if filename not str
    """
    if(isinstance(filename,str) and isinstance(objectToWrite,(dict,list,str))):
        directory = os.path.split(filename)[0]
        if(not os.path.isdir(directory)):
            try:
                os.makedirs(directory)
            except OSError:
                raise ValueError("os.path.split(filename)[0] = {} needs to be a valid os.path.isdir path".format(directory))
        try:
            myfile = open(filename, 'w+')
            myfile.write(json.dumps(objectToWrite))
            myfile.close()
        except IOError as eIO:
            raise eIO
    else:
        raise TypeError("filename type = {} and objectToWrite type {}".format(type(filename),type(objectToWrite)))

def WriteToCSVFile(path,headers,data):
    try:
        with open(path, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writerows(data)
    except Exception as e:
        raise e

def WriteArrayToFileWithDelimiter(filename,arrayToWrite, delimiter):
    """Writes array to file w/ delimiter

    Args:
        filename (str): valid path formatted str
        arrayToWrite (list()): Array to join with delimiter
        delimiter (char): delimiter to join array with

    Raises:
        IOError: If can't write to file then raises
        ValueError: if filename is not valid
        TypeError: if filename not str
    """
    dataToWrite = delimiter.join(arrayToWrite)
    WriteToFile(filename,dataToWrite)
    return dataToWrite

def GetListFromFolderOfExt(directoryPath, fileext): #TODO implement support for multiple ext's
    """Get List of files from folder

    Args:
        directoryPath (string): A path os.path formatted string to a direcotry
        fileext (string): '.*' formatted file extension preferred - Will insert '.' if no prefix found

    Raises:
        ValueError: if directoryPath is not valid dir or length files < 0
        TypeError: if directoyPath not str or fileext not str

    Returns:
        list(): filenames w/o fileext
    """
    if(isinstance(directoryPath,str) and isinstance(fileext,str)):
        if (not os.path.isdir(directoryPath)): # Check Folder Directory Exists
            raise ValueError("Need valid path formatted string for directoryPath")
        if (fileext[0] != '.'):
            fileext.insert(0,'.')

        output_list = []
        # Build List of filenames with ext
        for entry in scandir.scandir(directoryPath):
            if (entry.path.endswith(fileext)):
                filename = entry.name.replace(fileext, "")
                output_list.append(filename)
            elif (os.path.isdir(entry.path)):
                directoryList = GetListFromFolderOfExt(entry.path, fileext)
                output_list.extend(directoryList)
        return output_list
    else:
        raise TypeError("Type is wrong for: directoryPath = {} fileext = {}".format(type(directoryPath),type(fileext)))

def GetListFilenamePath(directoryPath, fileext): #TODO implement support for multiple ext's
    """Get Dict of filename and path from folder

    Args:
        directoryPath (string): A path os.path formatted string to a direcotry
        fileext (string): '.*' formatted file extension preferred - Will insert '.' if no prefix found

    Raises:
        ValueError: if directoryPath is not valid dir or length files < 0
        TypeError: if directoyPath not str or fileext not str

    Returns:
        dict(): filenames w/o fileext and path
    """
    if(isinstance(directoryPath,str) and isinstance(fileext,str)):
        if (not os.path.isdir(directoryPath)): # Check Folder Directory Exists
            raise ValueError("Need valid path formatted string for directoryPath")
        if (fileext[0] != '.'):
            fileext.insert(0,'.')
        outputList = list()
        # Build List of filenames with ext
        for entry in scandir.scandir(directoryPath):
            if (entry.path.endswith(fileext)):
                filename = entry.name.replace(fileext, "")
                outputList.append([filename,entry.path])
            # Drills down and extends filenames w/ fileext in subfolders
            elif (os.path.isdir(entry.path)):
                sub_directory_output = GetListFilenamePath(entry.path, fileext)
                outputList.extend(sub_directory_output)
        return outputList
    else:
        raise TypeError("Type is wrong for: directoryPath = {} fileext = {}".format(type(directoryPath),type(fileext)))

def GetDictFileCreationTimePath(directoryPath, fileExtToScrape):
    """Builds a dict() of {filename:[creation time,path to file]}

    Args:
        directoryPath (str): path formatted str to directory
        fileExtToScrape (str): ext to scrap for

    Raises:
        ValueError: if directoryPath is not a dir
        TypeError: if directoryPath or fileExtToScrtap are not str

    Returns:
        dict(): filenames with creation time and path
    """
    if(isinstance(directoryPath,str) and isinstance(fileExtToScrape,str)):
        # Check Folder Directory Exists and has files and Extention has . prefix and folder
        if (not os.path.isdir(directoryPath)):
            raise ValueError("Need valid Directory input. directoryPath = {}".format(directoryPath))
        if (fileExtToScrape[0] != '.'):
            fileExtToScrape.insert(0,'.')

        outputDict = dict()
        # Iterate each folder and file in directory. Build Dictionary of files with ext and store Modified Date/Path
        # Build List of filenames with ext
        for entry in scandir.scandir(directoryPath):
            if (entry.path.endswith(fileExtToScrape)):
                filename = entry.name.replace(fileExtToScrape, "")
                outputDict[filename] = [os.path.getctime(entry.path), entry.path]
            elif (os.path.isdir(entry.path)):
                print(entry.path + " is processing")
                outputDict = MergeDicts(outputDict, GetDictFileCreationTimePath(entry.path, fileExtToScrape))
            # else will skip any file not has fileExtToScrape and iterate through folders First in Last Out
        return outputDict
    else:
        raise TypeError("directory path type = {} | fileExtToScrape type = {}".format(type(directoryPath),type(fileExtToScrape)))

def BuildDictFromFolderWithExt(directoryPath, fileExtToScrape,includeDateCreated = True):
    """Build's a dictionary of files with paths and optional date created

    Args:
        directoryPath (str): an os.path.isdir valid formatted str 
        fileExtToScrape (str): a file ext to scrape the folder for
        includeDateCreated (bool, optional): [description]. Defaults to True.

    Raises:
        ValueError: Require a Directory formatted Path
        TypeError: require str,str,(optional)bool
        OSError: if trying to get ctime of file and no permissions or file doesn't exist

    Returns:
        dict: dict Keys = Filename value = path and optional cTime
    """
    # Check Folder Directory Exists and has files and Extention has . prefix and folder
    if(isinstance(directoryPath,str) and isinstance(fileExtToScrape,str) and isinstance(includeDateCreated,bool)):
        if (not os.path.isdir(directoryPath)):
            raise ValueError("Need valid Directory input")
        if (len(os.listdir(directoryPath)) == 0):
            return "Directory has no Files or Folders"
        if (fileExtToScrape[0] != '.'):
            fileExtToScrape.insert(0,'.')
        outputDict = dict()

        # Iterate each folder and file in directory. Build Dictionary of files with ext and store Modified Date/Path
        for directory in scandir.scandir(directoryPath):
            if (directory.path.endswith(fileExtToScrape)):
                filename = directory.name.replace(fileExtToScrape, "")
                if(includeDateCreated):
                    try:
                        outputDict[filename] = [os.path.getctime(directory.path), directory.path]
                    except OSError as inAccessiblefile:
                        raise inAccessiblefile
                else:
                    outputDict[filename] = [directory.path]
            elif (os.path.isdir(directory.path)):
                print(directory.path + " is processing")
                outputDict = Merge(outputDict, BuildDictFromFolderWithExt(directory.path, fileExtToScrape))
            # else will skip any file not has fileExtToScrape and iterate through folders First in Last Out
        return outputDict
    else:
        raise TypeError("Expecting str,str,bool. Got {},{},{}".format(type(directoryPath),type(fileExtToScrape),type(includeDateCreated)))

def RemoveFileAtPath(filePath):
    """Remove file at filepath

    Args:
        filePath (str): and os.path.isfile valid formatted path

    Raises:
        OSError: OS Error if file doesn't exist or no permissions to delete
        ValueError: if filePath not os.path.isfile valid formatted path
        TypeError: if filePath is not str
    """
    if(isinstance(filePath,str)):
        if(os.path.isfile(filePath)):
            try:
                os.remove(filePath)
                return None
            except OSError as inAccessiblefile:
                raise inAccessiblefile
        else:
            raise ValueError("filepath is not os.path.isfile valid. Got {}".format(filePath))
    else:
        raise TypeError("Expecting a str. Got {}".format(type(filePath)))

def RemoveFolderAtPath(folderPath,deleteFilesInFolder):
    """Removes a folder at path

    Args:
        folderPath (str): os.path.iddir valid formatted path
        deleteFilesInFolder (bool): delete files in folder automatically or not

    Raises:
        OSError: OS Error if file doesn't exist or inaccessible
        ValueError: if folderPath not os.path.isdir valid formatted path
        TypeError: if folderPath not str or deleteFilesInFolder not bool
    """
    if(isinstance(folderPath,str) and isinstance(deleteFilesInFolder,bool)):
        if(os.path.isdir(folderPath)):
            if(len(os.listdir(folderPath)) > 0 and deleteFilesInFolder):
                for file in scandir.scandir(folderPath):
                   RemoveFileAtPath(file.path) 
            try:
                os.rmdir(folderPath) # Error is thrown by system if folder is not empty
                return None
            except OSError as inAccessiblefile:
                raise inAccessiblefile
        else:
            raise ValueError("folderPath is not os.path.isdir valid. Got {}".format(folderPath))
    else:
        raise TypeError("Expecting a str. Got {}".format(type(folderPath)))

def CopyFileFromTo(filepathToCopy,destinationPath,makeDirToDestination = True):
    """Copy File from path to destination

    Args:
        filepathToCopy (str): an os.path.isfile valid formatted str
        destinationPath ([type]): an os.path.isdir valid formatted path
        makeDirToDestination (bool, optional): Make the directory to the destination file path. Defaults to True.

    Raises:
        osError: if you have no permissions for IO Operations
        ValueError: If not valid filepath or destination path
        TypeError: Expecting str,str,bool
    """
    if(isinstance(filepathToCopy,str) and isinstance(destinationPath,str) and isinstance(makeDirToDestination,bool)):
        if(os.path.isfile(filepathToCopy)):
            directory = os.path.split(destinationPath)[0]
            if(not os.path.isdir(directory) and makeDirToDestination):
                try:
                    os.makedirs(directory)
                except OSError as osError:
                    raise osError
            try:
                copy2(filepathToCopy,destinationPath)
            # If source and destination are same 
            except shutil.SameFileError: 
                raise ValueError("Source and destination represents the same file.") 
            # If there is any permission issue 
            except shutil.PermissionError: 
                raise ValueError("Permission denied.") 
            # For other errors 
            except: 
                print("Error occurred while copying file.") 
        else:
            raise ValueError("Expecting an os.path.isdir valid formatted path str. Got {}".format(filepathToCopy))
    else:
        raise TypeError("Expecting str,str,bool. Got {},{},{}".format(type(filepathToCopy),type(destinationPath),type(makeDirToDestination)))
    