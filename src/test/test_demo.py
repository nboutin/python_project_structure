'''
Created on 12 janv. 2021

@author: F24178C
'''
import unittest
from project.package_b.module_b1 import ModuleB1


class TestDemo(unittest.TestCase):

    def testDemo(self):
        _ = ModuleB1()
        self.assertTrue(True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
