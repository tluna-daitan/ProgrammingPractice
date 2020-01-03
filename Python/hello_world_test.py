import sys
import unittest
from calculator.hello_world import HellowWorld

class TestHelloWorld(unittest.TestCase):

    #def setUp(self):
    
    def test_helloWorld(self):
        test = HellowWorld()
        self.assertEqual("Hello World!", test.getGreetingText())

if __name__ == '__main__':
    unittest.main()