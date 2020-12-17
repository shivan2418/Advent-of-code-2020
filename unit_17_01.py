from collections import defaultdict
import itertools

input = '''.#.
..#
###
'''

def setup_matrix(input):
    cube_matrix = keydefaultdict(newcube,{})
    z = 0
    input = input.split('\n')

    for y,row in enumerate(input):
        for x,col in enumerate(row):
            active = False if col=='.' else True
            cube_matrix[(x,y,z)] = Cube(x,y,z,active)

    return cube_matrix

class Cube:
    matrix = None
    def __init__(self,x,y,z=0,active=False):
        self.x=x
        self.y=y
        self.z=z
        self.active=active

    def get_neighbours(self):
        base = (self.x,self.y,self.z)
        coordinates = []
        for mod in [1,-1]:
            for pos in range(3):
                new_b = list(base)
                new_b[pos]+=mod
                coordinates.append(tuple(new_b))

        neighbours = []
        for cor in coordinates:
            neighbours.append(Cube.matrix[cor])

        return neighbours

    def get_num_active_neighbours(self):
        neighbours = self.get_neighbours()
        return [n.active for n in neighbours].count(True)

    def get_pending_change(self):
        active_neighbours = self.get_num_active_neighbours()

        if self.active and active_neighbours in [2,3]:
            return True
        elif self.active and active_neighbours not in [2,3]:
            return False
        elif not self.active and active_neighbours == 3:
            return True
        elif not self.active and active_neighbours != 3:
            return False
        else:
            raise("Something wrong")

    @classmethod
    def run_round(self):
        pending_changes = {}
        for pos,cube in Cube.matrix.items():
            pending_changes[pos]=cube.get_pending_change()


        # apply the changes

        for pos,change in pending_changes.items():
            Cube.matrix[pos].active=change


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

def newcube(xyz):
    x,y,z = xyz
    cube = Cube(x,y,z)
    Cube.matrix[(x,y,z)]=cube
    return cube


Cube.matrix = setup_matrix(input)

for round in range(6):

    Cube.run_round()

print('a')