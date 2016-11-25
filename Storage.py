

class Storage:
    """ Maintains the storage layer of the hashes """
    map = dict()

    def __init__(self):
        self.map.clear()

    def store(self, uid, path_in):
        if uid in self.map:
            paths = self.map.get(uid)
            paths.add(path_in)
        else:
            paths = PathStorage(path_in)
        self.map[uid] = paths

    def contains(self, uid):
        return uid in self.map

    def numberOfUids(self, uid):
        return len(self.map.get(uid))

    def number_of_unique_uids(self):
        return len(self.map)

    def get_first_path(self, uid):
        return self.map.get(uid).first_path


class PathStorage:
    """ Maintains the actual list of paths """
    paths = []
    first_path = ""

    def __init__(self, first_path):
        self.paths = []
        self.first_path = first_path
        self.paths.append(first_path)

    def get_num_paths(self):
        return len(self)

    def add(self, path):
        self.paths.append(path)

    def __len__(self):
        return len(self.paths)