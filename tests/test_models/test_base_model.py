#!/usr/bin/python3
"""This module will be able to  handle all test cases related to the class
BaseModel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """This class defines tests cases for the BaseModel
    class
    """

    def setUp(self):
        """Set Up instances"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()

    def test_uuid(self):
        """UUID tests"""
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertIsInstance(self.bm1.id, str)
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_instance_type(self):
        """tests what the instance type is"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertIsInstance(str(self.bm1), str)
        self.assertEqual(str(self.bm2),
                        "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_to_dict(self):
        """tests the dictionary representation of an instance"""
        self.assertIsInstance(self.bm2.to_dict(), dict)

    def test_type_created_at(self):
        """tests if type of created time attribute is datetime"""
        self.assertIs(self.bm1.created_at, datetime)

    def test_type_updated_at(self):
        """tests if type of created time attribute is datetime"""
        self.assertIs(self.bm1.updated_at, datetime)
