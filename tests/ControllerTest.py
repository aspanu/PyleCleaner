import unittest
from Controller import Controller
from FileWalker import FileWalker


class ControllerTest(unittest.TestCase):

    def test_init(self):
        controller = Controller()
        # file_handler = FileWalker()
        # data_handle = file_handler.next_file()
        # controller.store_data(data_handle)

