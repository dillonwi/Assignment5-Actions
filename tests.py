import unittest
from unittest import TestCase

import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_get_area(self):
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

    def test_first_last(self):
        tList = [7, 5, 4, 3, 10]

        #Run the function
        rList = task.firstLast(tList)

        #Check to see that the right values were returned from the function
        self.assertEqual(rList[0], 7)
        self.assertEqual(rList[-1], 10)

        #Make a second list
        tList2 = list(range(1,15))

        rList = task.firstLast(tList2)

        # Check to see that the right values were returned from the function
        self.assertEqual(rList[0], 1)
        self.assertEqual(rList[-1], 14)

        pass


if __name__ == '__main__':
    unittest.main()
