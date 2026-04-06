# my_functions_test.py

import unittest
import my_functions

class UnitTestMathOperations(unittest.TestCase):
    
    def test_math_addition(self):
        '''Mathematische Addition testen'''
        result = my_functions.math_addition(2, 2)
        self.assertEqual(result, 4, "Die Addition sollte 4 ergeben")
    
    def test_math_division(self):
        '''Mathematische Division testen'''
        # normaler Fall — funktioniert die Division korrekt?
        result = my_functions.math_division(6, 2)
        self.assertEqual(result, 3, "Die Division sollte 3 ergeben")
        
        # Edge Case — wird Division durch 0 korrekt abgefangen?
        with self.assertRaises(ValueError):
            my_functions.math_division(10, 0)

if __name__ == '__main__':
    unittest.main()