from django.test import TestCase
import unittest


# Create your tests here.
class TestMyMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("Sankalp".upper(), "SANKALP")
        return 
    
    def test_isUpper(self):
        self.assertTrue("SANKALP".isupper())
        self.assertFalse("sankalp".isupper())
        return 
    
    def test_split(self):
        str = "Hello World."
        self.assertEqual(str.split(' '), ["Hello", "World."])
        with self.assertRaises(TypeError):
            str.split(2)
        return 
    
    
if __name__ == '__main__':
    unittest.main()