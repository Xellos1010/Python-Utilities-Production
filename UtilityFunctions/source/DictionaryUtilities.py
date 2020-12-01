from ErrorHandling import LogError

# Dictionary DataStructure Utility Functions
def MergeDicts(dict1, dict2): #TODO Refactor to take *args with dict's to combine more than 1 dict
    """Python Code to merge dicts first in last out

    Args:
        dict1 (dict()): Base dictionary
        dict2 (dict()): Dictionary to extend with

    Raises:
        TypeError: if dicts 1 & 2 are not dict()

    Returns:
       dict() : Merged dictionary
    """
    if(isinstance(dict1,dict) and isinstance(dict2,dict)):
        try:
            z = dict1.copy()  # start with x's keys and values
            z.update(dict2)  # modifies z with y's keys and values & returns None
            return z
        except Exception as e:
            LogError("Exception Occured: {}".format(e))
            return None
    else:
        raise TypeError("Expected a dict() you passed: {} or {}".format(type(dict1),type(dict2)))
    
class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, xrange):# python 3range): # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super(RangeDict,self)#Python3 .__getitem__(item) # or super(RangeDict, self) for Python 2
