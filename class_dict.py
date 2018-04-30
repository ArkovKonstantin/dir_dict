import os
import collections


class DirDict(collections.MutableMapping):
    def __init__(self, path):
        self.path = path

    def __getitem__(self, key):

        for file in os.listdir(self.path):
            if file.split('.')[0] == key:
                with open(self.path + file) as handler:
                    return handler.read().replace('\n', ' ')

    def __setitem__(self, key, value):

        for file in os.listdir(self.path):
            if file.split('.')[0] == key:
                with open(self.path + file, 'w') as handler:
                    handler.write(value)

    def __delitem__(self, key):
        for file in os.listdir(self.path):
            if file.split('.')[0] == key:
                os.remove(self.path + file)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(os.listdir(self.path))

    def values(self):
        for file in os.listdir(self.path):
            with open(self.path + file) as handler:
                yield handler.read().replace('\n', ' ')

    def keys(self):
        for file in os.listdir(self.path):
            yield file.split('.')[0]

    def items(self):
        for file in os.listdir(self.path):
            with open(self.path + file) as handler:
                yield (file.split('.')[0], handler.read().replace('\n', ' '))

    def clear(self):
        for file in os.listdir(self.path):
            os.remove(self.path + file)

    def get(self, key, default=None):
        for file in os.listdir(self.path):
            if file.split('.')[0] == key:
                with open(self.path + file) as handler:
                    return handler.read().replace('\n', ' ')
        else:
            return default

    def popitem(self):
        os.remove(self.path + os.listdir(self.path)[-1])

    def setdefault(self, key, default=None):
        for file in os.listdir(self.path):
            if file.split('.')[0] == key:
                with open(self.path + file) as handler:
                    return handler.read().replace('\n', ' ')

        else:
            with open(self.path + key, 'w') as handler:
                handler.write(default)

    def update(*args):  # self находится в args[0]
        print(args[0].path, args[1].path)
        for key1 in os.listdir(args[1].path):
            for key0 in os.listdir(args[0].path):
                if key1 == key0:
                    for new_key1 in os.listdir(args[1].path):
                        for new_key0 in os.listdir(args[0].path):
                            if new_key1 == new_key0:
                                with open(args[0].path + new_key0, 'w') as handler0:
                                    with open(args[1].path + new_key1) as handler1:
                                        handler0.write(handler1.read())
                                        break

                        else:
                            with open(args[0].path + new_key1, 'w') as handler0:
                                with open(args[1].path + new_key1) as handler1:
                                    handler0.write(handler1.read())
        else:
            return None

    def copy(self, new_path):
        if os.path.exists(new_path):
            for file in os.listdir(self.path):
                with open(self.path + file) as handler1:
                    with open(new_path + file, 'w') as handler2:
                        handler2.write(handler1.read())
            return DirDict(new_path)
        else:
            return None




