from os import path

def GetUserInputDirectory(msgForUser,test_output = ""):
    """allows user to input a directory

    Args:
        msgForUser (str): message to present to user in console 
        testOutput (str,optional): expected output from script

    Returns:
        str: path formatted str
        
    Raises:
        TypeError: msgForUser requires str
        ValueError: test_output either needs to be "" or dir formatted str
    """
    if(isinstance(msgForUser,str)):
        if(not test_output == ""):#Unit Testing Only
            if(path.isdir(test_output)):
                return test_output
            else:
                raise ValueError("test_output needs to be a dir formatted path. Got {}".format(test_output))
        output = test_output
        while output == "" or not path.isdir(output):
            output = raw_input(msgForUser)
            if(output[0]=='"'): # replace " with empty char
                output = output.replace('"','')
        return output
    else:
        raise TypeError("Expected str for msgForUser got {}".format(type(msgForUser)))

def GetUserInputFile(msgForUser,test_output = ""):
    """allows user to input a file

    Args:
        msgForUser (str): message to present to user in console

    Returns:
        str: path file formatted str
        
    Raises:
        TypeError: msgForUser requires str
        ValueError: test_output either needs to be "" or dir formatted str
    """
    if(isinstance(msgForUser,str)):
        if(not test_output == ""): #Unit Testing Only
            if(path.isfile(test_output)):
                return test_output
            else:
                raise ValueError("test_output needs to be a dir formatted path. Got {}".format(test_output))
        output = test_output
        while output == "" or not path.isfile(output):
            output = raw_input(msgForUser)
            if(output[0]=='"'): # replace " with empty char
                output = output.replace('"','')
        return output
    else:
        raise TypeError("Expected str for msgForUser got {}".format(type(msgForUser)))