import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for method: max_integer
    """

    def TestExpected(self):
        """
        Test the expected case, a list of positive integers
        """
        self.assertEqual(max_integer([5, 4, 3, 2, 1], 5))

    def TestNoneList(self):
        """
        Test case of empty list
        """
        self.assertIsNone(max_integer([]))
