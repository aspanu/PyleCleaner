import unittest
from UidFactory import UidFactory


class UidFactoryTest(unittest.TestCase):
    """ Test the UidFactory """
    TEST_PATH = "/sample/path"
    TEST_DATA1 = "sample data"
    TEST_DATA2 = "sample data 2"
    uid_factory = ""

    def setUp(self):
        self.uid_factory = UidFactory(self.TEST_PATH)
        self.uid_factory.add_data(self.TEST_DATA1)

    def test_compiles(self):
        self.assertTrue(True)

    def test_make_any_uid(self):
        uid_factory = UidFactory("")
        self.assertIsNone(uid_factory.make_uid())
        uid_factory = UidFactory(self.TEST_PATH)
        uid_factory.add_data(self.TEST_DATA1)
        self.assertIsNotNone(uid_factory.make_uid())

    def test_make_hash_uid(self):
        uid = self.uid_factory.make_uid()
        self.assertIsNot("", uid)

    def test_store_uid(self):
        first_uid = self.uid_factory.make_uid()
        second_uid = self.uid_factory.get_uid()
        self.assertEqual(first_uid, second_uid)

    def test_no_collision(self):
        self.uid_factory.add_data(self.TEST_DATA1)
        first_uid = self.uid_factory.make_uid()
        self.uid_factory.add_data(self.TEST_DATA2)
        second_uid = self.uid_factory.make_uid()
        self.assertNotEqual(first_uid, second_uid)

