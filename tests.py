import unittest
from unittest import TestCase
import math

import task


class TestCase(unittest.TestCase):

    def testl(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_get_area(self):
        #Initialize an area equal to 9 x pi.
        tArea = 9 * math.pi

         # Check to see that 9pi is equal to what comes out of passing 3 into the getArea function.
        self.assertEqual(tArea, task.getArea(3))

        # Set tArea to 25 pi
        tArea = 25 * math.pi

        # Check the running getArea with radius 5 returns 25 pi
        self.assertEqual(tArea, task.getArea(5))

        # Set tArea to 0
        tArea = 0

        # Check the running getArea with radius 0 returns 0
        self.assertEqual(tArea, task.getArea(0))

        pass

if __name__ == '__main__':
    unittest.main()
