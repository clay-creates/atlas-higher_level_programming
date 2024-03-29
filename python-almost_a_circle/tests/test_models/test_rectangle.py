#!/usr/bin/python3
"""
This module contains unittests for the Rectangle class
"""
import unittest
import os
import io
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        r = Rectangle(1, 2, 3)
        self.assertIsInstance(r, Rectangle)
        r = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r, Rectangle)

        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rectangle_properties(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_methods(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(), 2)
        self.assertEqual(str(r), "[Rectangle] (16) 3/4 - 1/2")

    def test_update(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(89, 1, 2, 3,4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 19, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    def test_create(self):
        r = Rectangle.create(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_display(self):
        r = Rectangle(1, 2, 3, 4)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n\n\n   #\n   #\n")

    def test_save_to_file(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, r.id)
        os.remove("Rectangle.json")

if __name__ == "__main__":
    unittest.main(exit=False)