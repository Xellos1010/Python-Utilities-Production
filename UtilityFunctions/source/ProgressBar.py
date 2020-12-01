import sys
__bar_length_max__ = 100 # internal max for bar length

def ProgressBarUpdate(value, end_value, operation_title, bar_length=20):
    """in-line visual update utility to provide script feedback on progress

    Args:
        value (int): current value out of end_value
        end_value (int): ending value for 100% reference
        operation_title (string): name of the Operation waiting for
        bar_length (int, optional): Length of the fillbar in cmd. Defaults to 20.

    Raises:
        ValueError: if value, end_value, or bar_length are not valid
        TypeError: if value != int, end_value != int, bar_length != int, operation_title != str

    Returns:
        str: progress bar string
    """
    #TODO: Implement float support
    if(isinstance(value,int) and isinstance(end_value,int) and isinstance(bar_length,int) and isinstance(operation_title,str)):
        if(value > -1 and end_value > 0 and bar_length <= __bar_length_max__ and bar_length > -1):
            if(value > end_value):
                value = end_value
                #TODO: Implement Warning Log
            percent = float(value) / end_value
            arrow = '-' * int(round(percent * bar_length)-1) + '>'
            spaces = ' ' * (bar_length - len(arrow))
            toWrite = "\r{2}: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100)),operation_title)
            sys.stdout.write(toWrite) # Writes the progressbar to 1 line with a Carriage return to overwrite the line 
            sys.stdout.flush() # Used to allow Carriage return to return on the same line 
            return toWrite # for testing outputs
        else:
            raise ValueError("value = {} < 0 | end_value = {} | bar_length = {}".format(value,end_value,bar_length))
    else:
        raise TypeError("Argument pass is not correct type. ({},{},{},{})".format(type(value),type(end_value),type(operation_title),type(bar_length)))
