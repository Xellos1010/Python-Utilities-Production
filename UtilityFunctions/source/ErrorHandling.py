import datetime
from FileSystemUtilities import WriteToFile

__errorsTracked__ = []
"""Used only in this script to track errors then write to file"""

def LogError(errorMessage,**kwargs):
    """Tracks errors throws from script

    Args:
        errorMessage (string): Error message to log
        **kwargs (dict()): error_type:Log,Warning,Exception

    Raises:
        TypeError: errorMe

    """
    if(isinstance(errorMessage,str)):
        print(errorMessage)
        __errorsTracked__.append(errorMessage)
        return None
    else:
        raise TypeError('Expected str for errorMessage. Got {}'.format(type(errorMessage)))

    
def WriteErrorsToFile():
    """Write errors to file and clear log"""
    if(not __errorsTracked__ is None):
        if(len(__errorsTracked__)>0):
            formattedLogName = '_'.join["ErrorLog","GarageChecker",datetime.date,datetime.time]
            WriteToFile(formattedLogName,__errorsTracked__)
            __errorsTracked__ = []