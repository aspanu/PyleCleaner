import unittest
from Controller import Controller
from FileHandler import FileHandler


class ControllerTest(unittest.TestCase):

    def test_init(self):
        controller = Controller()
        file_handler = FileHandler()
        data_handle = file_handler.next_file()
        controller.store_data(data_handle)