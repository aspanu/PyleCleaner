from os.path import isdir


class FileWalker:
    base_path = ""
    paths_visited = []
    initial_path = ""
    __current_path = ""

    def __init__(self, base_path, initial_path):
        self.paths_visited = []
        self.base_path = base_path
        self.initial_path = initial_path

    def next_file(self):
        if not isdir(self.__current_path):
            pass
        return FileHandle(self.initial_path)


class FileHandle:
    __file_handle = ""
    path = ""

    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path
