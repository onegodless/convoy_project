# -*- coding: latin1 -*-
'''
Created on May 28, 2018

@author: Jesús Molina 
'''
import unittest
from convoy_project.resources import Resources

class Test(unittest.TestCase):

    
    def setUp(self):
        self.inst_resources = Resources(10,20)

    def tearDown(self):
        pass


    def testName(self):
        pass

    def test_printing(self):
        print self.inst_resources

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()