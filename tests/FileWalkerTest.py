import unittest

from FileWalker import FileWalker


class FileWalkerTest(unittest.TestCase):
    BASE_PATH = "/path/1"
    INIT_PATH = "/path/2"

    def test_init(self):
        file_walker = FileWalker(base_path=self.BASE_PATH, initial_path=self.INIT_PATH)
        file_walker.paths_visited = []
        self.assertEqual(file_walker.base_path, self.BASE_PATH)
        self.assertEqual(file_walker.initial_path, self.INIT_PATH)

    # def test_get_fileHandle(self):
    #     file_walker = FileWalker(self.BASE_PATH, self.INIT_PATH)
    #     file_handle = file_walker.next_file()
    #     path = file_handle.get_path()
    #     self.assertTrue(self.INIT_PATH in path)
    #     file_handle = file_walker.next_file()
    #     path2 = file_handle.get_path()
    #     self.assertNotEqual(path, path2)