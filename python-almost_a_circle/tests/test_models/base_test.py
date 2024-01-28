#!/usr/bin/python3
"""
This module contains unittesting for the base module
"""
import unittest
import json
import os
from models.base import Base



class TestBase(unittest.TestCase):

    def test_auto_assign(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)

    def test_passed_id(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), "[{\"id\": 12}]")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{"id": 89}])

if __name__ == "__main__":
    unittest.main()