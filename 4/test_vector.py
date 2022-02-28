import unittest
from vector import Vector


class TestVector(unittest.TestCase):

    def test_constructor(self):
        """test constructor"""

        v = Vector(1, 2, 3)

        self.assertEqual(v.x, 1, "should set x correctly")
        self.assertEqual(v.y, 2, "should set y correctly")
        self.assertEqual(v.z, 3, "should set z correctly")


    def test_eq(self):
        """test equal operator"""
        v = Vector(1, 2, 3)

        self.assertTrue(v == Vector(1, 2, 3), "should return true when all x, y and z are equal")
        self.assertFalse(v == Vector(0, 2, 3), "should return false when x differs")
        self.assertFalse(v == Vector(1, 0, 3), "should return false when y differs")
        self.assertFalse(v == Vector(1, 2, 0), "should return false when z differs")


    def test_add_scalar(self):
        """test add operator with scalar values"""

        v = Vector(1, 2, 3)

        self.assertEqual(v + 5, Vector(6, 7, 8), "should add n to every component")


    def test_add_vector(self):
        """test add operator with another vector"""

        v = Vector(1, 2, 3)
        u = Vector(4, 5, 6)

        self.assertEqual(v + u, Vector(5, 7, 9), "should add component by component")


    def test_sub_scalar(self):
        """test sub operator with scalar values"""

        v = Vector(1, 2, 3)

        self.assertEqual(v - 5, Vector(-4, -3, -2), "should subtract n to every component")


    def test_sub_vector(self):
        """test sub operator with another vector"""

        v = Vector(1, 2, 3)
        u = Vector(4, 3, 2)

        self.assertEqual(v - u, Vector(-3, -1, 1), "should subtract component by component")

    def test_mul_scalar(self):
        """test mul operator with scalar values"""

        v = Vector(1, 2, 3)

        self.assertEqual(v * 2, Vector(2, 4, 6), "should multiply n to every component")

    def test_mul_vector(self):
        """test mul operator with another vector"""

        v = Vector(1, 2, 3)
        u = Vector(4, 5, 6)

        self.assertEqual(v * u, Vector(-3, 6, -3), "should calculate cross product correctly")

    def test_mod_scalar(self):
        """test mod operator with scalar values"""

        v = Vector(1, 2, 3)

        self.assertEqual(v % 2, Vector(1, 0, 1), "should mod n to every component")

    def test_mul_vector(self):
        """test mod operator with another vector"""

        v = Vector(1, 2, 3)
        u = Vector(4, 5, 6)

        self.assertEqual(v % u, 32, "should calculate dot product correctly")

