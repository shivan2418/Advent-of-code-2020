from collections import defaultdict

input = '''
.#.
..#
###
'''
class Cube:
    def __init__(self,x,y,z=0,active=False):
        self.x=x
        self.y=y
        self.z=z
        self.active=active

    def get_neighbours(self):
        pass

    def __str__(self):
        return f"{self.x}-{self.y}-{self.z} {self.active}"

    def __repr__(self):
        return self.__str__()

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret



