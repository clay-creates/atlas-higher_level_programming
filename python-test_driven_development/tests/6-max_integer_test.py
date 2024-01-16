#!/usr/bin/python3
"""
This module contains the implementation of unittesting for max_integer(list=[])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for method: max_integer
    """

    def test_mixed(self):
        """
        Test case for list with positive and negative integers
        """
        self.assertEqual(max_integer([-1, 2, -3, 4, -5], 4))

    def test_max_end(self):
        """
        Test case for max int at end of list
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5], 5))

    def test_max_start(self):
        """
        Test case for max int at start of list
        """
        self.assertEqual(max_integer([5, 4, 3, 2, 1], 5))

    def test_max_mid(self):
        """
        Test case for max int in middle of list
        """
        self.assertEqual(max_integer([1, 2, 5, 3, 4], 5))

    def test_single_negative(self):
        """
        Test case for a single negative integer in list
        """
        self.assertEqual(max_integer([]))

    def test_all_negative(self):
        """
        Test case for list of only negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5], -1))

    def test_none(self):
        """
        Test case of empty list
        """
        self.assertIsNone(max_integer([]))
