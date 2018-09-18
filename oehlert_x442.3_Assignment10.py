#!/usr/bin/env python3

from collections import UserList
from collections import UserDict


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length


r = Rectangle(2, 5)
rp = r.perimeter()
ra = r.area()

print("Perimeter is {} and area is {}".format(rp, ra))


class UList(UserList):
    def add_iterable(self, iterable):
        for i in iterable:
            if i not in self:
                UserList.append(self, i)
        return self

    def __add__(self, blob):
        if hasattr(blob, "__iter__"):
            return self.add_iterable(blob)
        else:
            return self.data.append(self, blob)

    def append(self, blob):
        if blob not in self.data:
            self.data.append(blob)
        return self

    def extend(self, blob):
        return self.add_iterable(blob)


u = UList([5, 6, 7])
u2 = UList([1, 2, 3, 4])

print(u2.__add__(u))
print(u.extend(u2))
print(u.append(8))


class ODict(UserDict):
    def __init__(self):
        self.data = {}
        self.keys = []

    def __setitem__(self, key, value):
        self.data[key] = value
        self.keys.append(key)

    def okeys(self):
        return self.keys


d = ODict()
d["s"] = "1.0"
d["a"] = "red"
d["m"] = "5"

print(d.okeys())
