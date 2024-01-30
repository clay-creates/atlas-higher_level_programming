#!/usr/bin/python3
"""
This module contains unittests for the Square class
"""
import unittest
import io
import sys
import os
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square (1, 2, 3)

        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)
        self.assertIsInstance(s3, Square)

        with self.assertRaises(TypeError):
            s = Square("1")
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_square_properties(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 4, 'size': 1, 'x': 2, 'y': 3})

    def test_update(self):
        s = Square(1, 2, 3, 4)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_create(self):
        s = Square.create(id=1, size=2, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_save_to_file(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", 'r') as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", 'r') as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Square.json")

    def test_load_from_file(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, s.id)
        os.remove("Square.json")

    def test_display_without_xy(self):
        s = Square(1)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n")

    def test_display_without_y(self):
        s = Square(1, 2)
        output = io.StringIO()
        sys.stdout = output
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  #\n")

if __name__ == "__main__":
    unittest.main()