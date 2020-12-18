from collections import defaultdict
import itertools

input = '''.#.
..#
###
'''

def setup_matrix(input):
    cube_matrix = {}
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

    @property
    def pos(self):
        return (self.x,self.y,self.z)

    @property
    def value(self):
        if self.active:
            return '#'
        else:
            return '.'

    def _get_neighbour_coordinates(self):
        base = (self.x, self.y, self.z)
        coordinates = []
        for mod in [1, -1]:
            for pos in range(3):
                new_b = list(base)
                new_b[pos] += mod
                coordinates.append(tuple(new_b))
        return coordinates

    def get_neighbours(self):
        coordinates = self._get_neighbour_coordinates()
        neighbours = []
        for cor in coordinates:
            try:
                neighbour_cube = Cube.matrix[cor]
            except KeyError:
                # create a new cube and return that
                neighbour_cube = Cube(*cor)
            neighbours.append(neighbour_cube)

        return neighbours

    def get_num_active_neighbours(self):
        coordinates = self._get_neighbour_coordinates()

        status = []

        for cor in coordinates:
            try:
                cube = Cube.matrix[cor]
                status.append(cube.active)
            except KeyError:
                status.append(False)

        return status.count(True)

    def get_pending_change(self):
        active_neighbours = self.get_num_active_neighbours()

        if self.active and active_neighbours in [2,3]:
            return None # no change
        elif self.active and active_neighbours not in [2,3]:
            return False
        elif not self.active and active_neighbours == 3:
            return True
        elif not self.active and active_neighbours != 3:
            return None
        else:
            raise("Something wrong")

    @classmethod
    def total_active(cls):
        return [c.active for c in Cube.matrix.values()].count(True)

    @classmethod
    def expand_cube(cls,rounds):

        for _ in range(rounds):
            # make new cubes at the edges
            neighbours = []
            for cube in Cube.matrix.values():
                c = cube.get_neighbours()
                neighbours.extend(c)
            for n in neighbours:
                if n.pos not in Cube.matrix.keys():
                    Cube.matrix[n.pos] = n

            print(f'Total cubes: {len(Cube.matrix)}')

    @classmethod
    def run_round(self):

        neighbours_coordinates=[]
        for cube in Cube.matrix.values():
            neighbours_coordinates.append(cube._get_neighbour_coordinates())

        pending_changes = {}
        for pos,cube in Cube.matrix.items():
            pending_changes[pos]=cube.get_pending_change()

        # keep only not none changes
        pending_changes = {k:v for k,v in pending_changes.items() if v is not None}

        # apply the changes
        for pos,change in pending_changes.items():
            Cube.matrix[pos].active=change


        Cube.print_map()

    @classmethod
    def print_map(self):
        z_levels = {c.z for c in Cube.matrix.values()}
        for z in sorted(list(z_levels)):
            print(f"Z-level: {z}")
            cubes_on_z_level = [c for c in Cube.matrix.values() if c.z == z]
            y_levels = {c.y for c in cubes_on_z_level}
            for y in y_levels:
                cubes_on_y = [c for c in cubes_on_z_level if c.y==y]
                cubes_on_y.sort(key=lambda c:c.x)
                print(''.join([c.value for c in cubes_on_y]))



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

Cube.matrix = setup_matrix(input)


Cube.expand_cube(6)

for round in range(6):

    Cube.run_round()
print(Cube.total_active())

