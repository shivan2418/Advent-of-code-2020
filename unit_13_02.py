from elutils.decorators import timeit

small_input='''939
7,13,x,x,59,x,31,19'''
full_input = '''1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41'''
very_small_input = '''17,x,13,19'''

def bus_line_generator(bus_id,start_pos=0):
    '''Keeps generating the times where the bus depart'''
    dep_t = start_pos
    while True:
        dep_t += bus_id
        yield dep_t

def bus_departs_at_timestamp(bus,timestamp):
    return timestamp%bus==0

the_input = very_small_input

def parse_input(input_string):
    try:
        departure_time = int(input_string.split('\n')[0])
    except:
        pass
    bus_schedules_time = input_string.split('\n')[-1].split(',')
    x_count = 0
    offset_from_t = {}
    for b in bus_schedules_time:
        if b == 'x':
            pass
        else:
            offset_from_t[int(b)] = x_count
        x_count += 1

    return offset_from_t

@timeit
def find_timestamp_setup(input_string):

    offset_from_t= parse_input(input_string)
    first_bus = [v for v in offset_from_t.keys()][0]

    return find_timestamps(first_bus,0,offset_from_t)


def find_timestamps(step,startpos,offset_dict):
    generator = bus_line_generator(step,startpos)
    previous = []
    for timestamp in generator:
        departures= {}
        for bus,offset in offset_dict.items():
            departs = bus_departs_at_timestamp(bus,timestamp+offset)
            if departs:
                departures[bus] = departs
                if len(departures) == 2:
                    previous.append(timestamp)
                    if len(previous)==2:
                        step = previous[-1]-previous[-2]
                        startpos = previous[-1]
                        new_offset_dict = {k:v for k,v in offset_dict.items() if k not in departures}
                        return find_timestamps(step,startpos,new_offset_dict)

            else:
                break
        else:
            if all([v for v in departures.values()]):
                offset_of_least = list(offset_dict.values())[0]
                print(f"answer is {timestamp+offset_of_least}")
                return timestamp

assert find_timestamp_setup('17,x,13,19') == 3417
assert find_timestamp_setup("67,7,59,61") == 754018
assert find_timestamp_setup("67,x,7,59,61") == 779210
assert find_timestamp_setup("67,7,x,59,61") == 1261476
assert find_timestamp_setup("1789,37,47,1889") == 1202161486

find_timestamp_setup(full_input)