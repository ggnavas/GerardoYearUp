#importing unittest library
import unittest






#this is where the Unit Test Goes for testing the functions.

#making a class for functions to test
class TestStringMethods(unittest.TestCase):

    #function to test upper case letter
    def test_upper(self):
        #testing to see if the expressions are equal
        self.assertEqual("foo".upper(),'FOO')

    #Another function for testing upper case
    def test_isupper(self):
        #testing to see if the expression is true
        self.assertTrue('FOO'.isupper())
        #testing to see if the expression is false
        self.assertFalse('foo'.isupper())
    
    #checking for string split
    def test_split(self):

        #create a string variable
        s = 'hello world'
        #testing to see if there's a space in between hello and world
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when the seperator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
#calling on the functions
if __name__ == '__main__':
    unittest.main()