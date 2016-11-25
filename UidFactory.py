import hashlib


class UidFactory:
    """ Create a uid from file input """
    __path = ""
    __uid = ""
    __hash = ""

    def __init__(self, path_in):
        self.__path = path_in
        self.__hash = hashlib.new("sha512")

    def make_uid(self):
        if self.__path == "":
            return None
        self.__uid = self.__hash.digest()
        return self.__uid

    def get_uid(self):
        return self.__uid


    def add_data(self, line):
        self.__hash.update(line.encode("utf-8"))
