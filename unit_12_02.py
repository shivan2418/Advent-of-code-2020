small_sample= """F10
N3
F7
R90
F11"""

f = open("day_12.txt")
full_sample = f.read()


import re
import itertools

# setup and helper methods
def get_compas(start_dir,direction):
    nesw =  ['N','E','S','W']

    if direction =='R':
        compas_dir = nesw
    elif direction == 'L':
        compas_dir = reversed(nesw)

    compas = itertools.cycle(compas_dir)
    # wind the compas to the correct position
    last = next(compas)
    while last != start_dir:
        last = next(compas)
    return compas

def parse_instruction(instruction) -> tuple:
    m = re.match(r"([A-Z]{1})([\d]+)",instruction)
    return (m.group(1),int(m.group(2)))

def convert_instructions(instruction):
    action, value = instruction
    if action == 'W':
        return ('E', value * -1)

    if action == 'S':
        return ("N", value * -1)
    return (action, value)

class Ship():

    def __init__(self):
        self.location ={'N':0,'E':0}
        self.facing_direction = "E"
        self.waypoint = {"E":10,"N":1}

    def rotate_waypoint(self,waypoint_facing,instruction):
        action, value = instruction
        times_to_turn = int(value / 90)
        compas = get_compas(waypoint_facing,action)
        new_direction = waypoint_facing
        for i in range(times_to_turn):
            new_direction = next(compas)

        return new_direction

    def get_new_facing_direction(self,instruction):
        action, value = instruction
        times_to_turn = int(value / 90)

        new_direction = self.facing_direction

        compas = get_compas(self.facing_direction,action)
        for i in range(times_to_turn):
            new_direction = next(compas)

        return new_direction

    def process_instruction(self,instruction):
        action,value = instruction

        if action in ['N','S']:
            self.waypoint['N']+=value
        elif action in ['E',"W"]:
            self.waypoint['E']+=value
        elif action in ['R','L']:
            # rotate the waypoint
            replace_keys= {}
            for key in self.waypoint.keys():
                new_direction = self.rotate_waypoint(key,instruction)
                replace_keys[new_direction]=self.waypoint[key]

            if 'S' in replace_keys.keys():
                replace_keys['N'] = replace_keys.pop('S')
                replace_keys['N'] = replace_keys['N']*-1
            if 'W' in replace_keys.keys():
                replace_keys['E'] = replace_keys.pop('W')
                replace_keys['E'] = replace_keys['E']*-1

            self.waypoint=replace_keys

        elif action == 'F':
            #move towards the waypoint
            for _ in range(value):
                for key,value in self.waypoint.items():
                    self.location[key]+=value
        else:
            raise("Something wrong")

    def get_manhatten_distance(self):
        return abs(self.location['N'])+abs(self.location['E'])

# parse instructions and convert S to negative north and W to negative east.
sample = full_sample.split('\n')
sample = [parse_instruction(i) for i in sample]
sample = [convert_instructions(i) for i in sample]

ship = Ship()

for i in sample:
    ship.process_instruction(i)
else:
    print(ship.get_manhatten_distance())