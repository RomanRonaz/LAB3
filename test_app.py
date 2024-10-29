import unittest
from app import add, invert_string

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_invert_string(self):
        self.assertEqual(invert_string("hello"), "olleh")
        self.assertEqual(invert_string(""), "")

if __name__ == "__main__":
    unittest.main()
