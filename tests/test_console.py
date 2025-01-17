#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import os
import unittest
from datetime import datetime
import console
import json

HBNBCommand = console.HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', '') == "db", "db")
class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCommand interpreter for Holberton AirBnB project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Command inerpreter class'
        actual = HBNBCommand.__doc__
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import os
import unittest
from datetime import datetime
import console
import json

HBNBCommand = console.HBNBCommand


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', '') == "db", "db")
class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nCommand interpreter for Holberton AirBnB project\n'
        actual = console.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Command inerpreter class'
        actual = HBNBCommand.__doc__
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main
