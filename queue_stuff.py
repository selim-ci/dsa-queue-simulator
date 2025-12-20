import time


# basic queue thing for cars
class Q:
    def __init__(self):
        self.items = []

    def put(self, x):
        self.items.append(x)

    def get(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return None

    def sz(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0


# car object
class Car:
    def __init__(self, i, ln, d='S'):
        self.i = i
        self.ln = ln
        self.d = d  # direction
        self.t = time.time()


# lane thing
class Ln:
    def __init__(self, nm, pr=False):
        self.nm = nm
        self.q = Q()
        self.pr = pr  # is it priority
        self.cnt = 0# fix
# more stuff
# fix
# more stuff
# fix
# more stuff
# fix
# more stuff
