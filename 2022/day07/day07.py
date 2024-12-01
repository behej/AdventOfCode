#! /usr/bin/python3

from itertools import chain

class Folder:
    def __init__(self, name):
        self.__name__ = name
        self.__folders__ = {}
        self.__files__ = []

    def __repr__(self):
        return "Folder {} contains {} subfolders and {} files. Total size={}"\
            .format(self.__name__, len(self.__folders__), len(self.__files__), self.size())

    def __getitem__(self, name):
        return self.__folders__[name]

    def __add__(self, o):
        return self.size() + o.size()

    def __radd__(self, o):
        if isinstance(o, int):
            return o + self.size()
        else:
            print("else")
            return self.__add__(o)

    def folders(self):
        return self.__folders__.values()

    def parent(self):
        return self.__parent__

    def add_dir(self, subd):
        self.__folders__[subd] = Folder(subd)
        self.__folders__[subd].__parent__ = self

    def add_file(self, size):
        self.__files__.append(size)

    def size(self):
        return sum(self.__files__) + sum(self.folders())

#######################################################

def sum_size(f):
    s = f.size() if f.size() <= limit else 0
    s += sum([sum_size(i) for i in f.folders()])
    return s


def list_sizes(f):
    l = [f.size()]
    l.extend(chain(*[list_sizes(i) for i in f.folders()]))
    return l

#######################################################

limit = 100000
total = 70000000
required = 30000000
root = Folder('/')
current = root


with open("input", "r") as f:
    for l in f:
        if l.strip() == '$ cd /':
            current = root
        elif l.strip() == '$ cd ..':
            current = current.parent()
        elif l.startswith('$ cd'):
            sub = l.split()[-1]
            current = current[sub]
        elif l.startswith('dir'):
            current.add_dir(l.split()[-1])
        elif l.split()[0].isdigit():
            current.add_file(int(l.split()[0]))


# Part 1
s = sum_size(root)
print("Part 1: {}".format(s))

# Part 2
available = total - root.size()
to_recover = required - available
sizes = list_sizes(root)
sizes = [s for s in sizes if s >= to_recover]
sizes.sort()

print("Part 2: {}".format(sizes[0]))
