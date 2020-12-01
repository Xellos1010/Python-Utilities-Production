import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
utility_functions_dir = os.path.join(parentdir,'source','UtilityFunctions')
sys.path.append(utility_functions_dir)

from ProgressBar import ProgressBarUpdate,__bar_length_max__

class MainTests(unittest.TestCase):
    ##Progress Bar Tests##
    #0% Fill Test
    def test_no_fill(self):
        self.assertEqual(ProgressBarUpdate(0,1,'TestBar',20),'\rTestBar: [>                   ] 0%') # What happens when value is set < end_value & bar_length = 20
    #1000% fill test
    def test_overfill(self):
        self.assertEqual(ProgressBarUpdate(100,1,'TestBar',20),'\rTestBar: [------------------->] 100%') # What happens when value is set over end_value
    #0% fill 0 Bar Length
    def test_no_fill_no_bar(self):
        self.assertEqual(ProgressBarUpdate(0,1,'TestBar',0),'\rTestBar: [>] 0%') # What returns when bar_length is set to 0?
    ##Raise Error Tests##
    #Type Error Tests
    def test_title_type_not_string(self):
        with self.assertRaises(TypeError):
            ProgressBarUpdate(0,1,5243) #this is TypeError (operation_title needs to be str)

    def test_endvalue_not_string(self):
        with self.assertRaises(TypeError):
            ProgressBarUpdate(0,'1','TestBar') #this is TypeError (end_value needs to be int)

    def test_value_not_string(self):
        with self.assertRaises(TypeError):
            ProgressBarUpdate('0',1,'TestBar') #this is TypeError (value needs to be int)

    def test_bar_length_not_string(self):
        with self.assertRaises(TypeError):
            ProgressBarUpdate(0,1,'TestBar','20') #this is TypeError (bar_length needs to be int)
    ##
    #ValueError Tests
    def test_negative_bar_length(self):
        with self.assertRaises(ValueError):
            ProgressBarUpdate(0,1,'TestBar',-1) #What returns when bar_length is < 0?

    def test_negative_endvalue(self):
        with self.assertRaises(ValueError):
            ProgressBarUpdate(0,-1,'TestBar') # this is ValueError (end value needs to be > 0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            ProgressBarUpdate(-1,0,'TestBar') # this is ValueError (value needs to be > 0)

    def test_bar_length_exceed_internal_max(self):
        with self.assertRaises(ValueError):
            print('__bar_length_max__ = {}'.format(__bar_length_max__))
            ProgressBarUpdate(-1,0,'TestBar',__bar_length_max__+1) # this is a ValueError (value of bar_length needs to be < __bar_length_max__)

    ####
if __name__ == "__main__":
    unittest.main()
