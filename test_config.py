import unittest

from config import Config


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Config.get_prop('jdbc.username'), 'root')


if __name__ == '__main__':
    unittest.main()
