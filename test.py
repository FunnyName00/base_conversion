import main
import unittest

class TestConversionFunctions(unittest.TestCase):

    def test_binTo10(self):
        self.assertEqual(main.binTo10(00000000), 0)
        self.assertEqual(main.binTo10(11111111), 255)
        
    def test_decimalToBinary(self):
        self.assertEqual(main.decimalToBinary(0), -1)
        self.assertEqual(main.decimalToBinary(222), 11011110)

class TestUtilsFunctions(unittest.TestCase):

    def test_lstToInt(self):
        self.assertEqual(main.lstToInt([0, 0, 0, 0]), 0000)
        self.assertEqual(main.lstToInt([]), -1  )

        
if __name__ == '__main__':
    unittest.main()