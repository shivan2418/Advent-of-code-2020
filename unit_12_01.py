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
            self.location['N']+=value
        elif action in ['E',"W"]:
            self.location['E']+=value
        elif action in ['R','L']:
            new_facing = self.get_new_facing_direction(instruction)
            self.facing_direction = new_facing
        elif action == 'F':
            if self.facing_direction=='S':
                self.location['N']-=value
            elif self.facing_direction=='W':
                self.location['E']-=value

            else: # East, North
                self.location[self.facing_direction]+=value
        else:
            raise("Something wrong")

    def get_manhatten_distance(self):
        a,b = list(self.location.values())
        return abs(a)+abs(b)


sample = full_sample.split('\n')
sample = [parse_instruction(i) for i in sample]
sample = [convert_instructions(i) for i in sample]

ship = Ship()

for i in sample:
    ship.process_instruction(i)
else:
    print(ship.get_manhatten_distance())