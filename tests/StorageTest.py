import unittest
from Storage import Storage


class StorageTest(unittest.TestCase):

    def test_initilization(self):
        storage = Storage()
        self.assertIsNotNone(storage.map)

    def test_storage(self):
        storage = Storage()
        storage.store("1", "/path/1")
        self.assertTrue(storage.contains("1"))
        self.assertEquals(1, storage.number_of_uids("1"))
        storage.store("2", "/other/path")
        self.assertTrue(storage.contains("2"))
        self.assertEquals(1, storage.number_of_uids("2"))
        self.assertEquals(2, storage.number_of_unique_uids())

    def test_storage_lists(self):
        storage = Storage()
        storage.store("1", "/path/1")
        storage.store("1", "/path/2")
        self.assertTrue(storage.contains("1"))
        self.assertEquals(2, storage.number_of_uids("1"))
        self.assertEquals(1, storage.number_of_unique_uids())
        self.assertEquals("/path/1", storage.get_first_path("1"))

