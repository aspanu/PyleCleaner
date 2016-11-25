import unittest
from Storage import PathStorage


class PathStorageTest(unittest.TestCase):
    PATH_ONE = "/path/1"
    paths = {}

    def setUp(self):
        self.paths = PathStorage(self.PATH_ONE)

    def test_init(self):
        self.assertEquals(self.PATH_ONE, self.paths.first_path)
        self.assertEquals(1, self.paths.get_num_paths())

    def test_create_paths(self):
        self.paths.add("/path/2")
        self.assertEquals(2, self.paths.get_num_paths())

    def test_create_multi_paths(self):
        for x in range(0, 100):
            self.paths.add(self.PATH_ONE)
        self.assertEquals(101, self.paths.get_num_paths())
