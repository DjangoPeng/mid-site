'''
Created on 2015-08-29

@author: y0022599
'''

from huawei.demo import Demo
import unittest

class Test(unittest.TestCase):
      
    def testValue(self):
        self.demo = Demo()
		stones_list = [1,2,3]
        x,y = self.demo.demo(stones_list)
        self.assertEqual(x, 9)
        self.assertEqual(y, 11)

                                                             
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testValue']
    unittest.main()
