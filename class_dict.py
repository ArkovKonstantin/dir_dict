import os
import collections


class DirDict(collections.MutableMapping):
    def __init__(self, path):
        self.path = path

    # Если такого файла нет вызваем исключение, иначе возвращаем содержимое
    def __getitem__(self, key):
        try:
            with open(os.path.join(self.path, key)) as handler:
                return handler.read()
        except FileNotFoundError:
            raise KeyError

    # Перезаписываем существующий файл, если такого файла нет, то создаем его
    def __setitem__(self, key, value):
        with open(os.path.join(self.path, key), 'w') as handler:
            handler.write(value)

    # Удаляем файл, если его нет вызываем исключение
    def __delitem__(self, key):
        try:
            os.remove(os.path.join(self.path, key))
        except FileNotFoundError:
            raise KeyError

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(os.listdir(self.path))

    # Метод возвращает генератор, который возвращает сод-ое файлов
    def values(self):
        for file in os.listdir(self.path):
            with open(os.path.join(self.path, file)) as handler:
                yield handler.read()

    # Метод возвращает генератор, который возвращает имя файлов
    def keys(self):
        for file in os.listdir(self.path):
            yield file

    # Метод возвращает генератор, который возвращает имя файла - содержимое
    def items(self):
        for file in os.listdir(self.path):
            with open(os.path.join(self.path, file)) as handler:
                yield (file, handler.read())

    # Метод удаляет все содержимое директории
    def clear(self):
        for file in os.listdir(self.path):
            os.remove(os.path.join(self.path, file))

    # Метод вернет сод-ое файла, если такого файла нет, то вернет default
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    # Метод удаляет последний файл в директории
    def popitem(self):
        os.remove(os.path.join(self.path, os.listdir(self.path)[-1]))

    # Метод возвращает сод-ое файла если его нет, то содает и пишет в него default
    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default

    # Обновляет директорию
    def update(self, new_dict):
        for key in new_dict.keys():
            self[key] = new_dict[key]

    # Копирует содержимое текущей директории в указанную
    def copy(self, new_path):
        if os.path.exists(new_path):
            new_dict = DirDict(new_path)
            for key, data in self.items():
                new_dict[key] = data
            return new_dict
        else:
            return None



