from Storage import Storage
from UidFactory import UidFactory


class Controller:
    storage = {}

    def __init__(self):
        self.storage = Storage()

    def store_data(self, file_handle):
        uid_factory = UidFactory(file_handle.get_path())