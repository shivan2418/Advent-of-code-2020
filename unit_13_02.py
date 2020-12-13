import elutils
from elutils.decorators import timeit

small_input='''939
7,13,x,x,59,x,31,19'''
full_input = '''1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41'''
very_small_input = '''17,x,13,19'''

def bus_line_generator(bus_id):
    '''Keeps generating the times where the bus depart'''
    dep_t = 0
    while True:
        dep_t += bus_id
        yield dep_t

def bus_departs_at_timestamp(bus,timestamp):
    return timestamp%bus==0

the_input = very_small_input


@timeit
def find_timestamp(input_string):
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
            offset_from_t[int(b)]=x_count
        x_count += 1

    # center on largest_value
    least_freq_running_bus = max([v for v in offset_from_t.keys()])
    offset_centered_on_least = {k:v-offset_from_t[least_freq_running_bus] for k,v in offset_from_t.items()}

    source_bus_line = bus_line_generator(least_freq_running_bus)
    for timestamp in source_bus_line:
            departures= {}
            for bus,offset in offset_centered_on_least.items():
                departs = bus_departs_at_timestamp(bus,timestamp+offset)
                if departs:
                    departures[bus]= departs
                else:
                    break
            else:
                if all([v for v in departures.values()]):
                    offset_of_least = list(offset_centered_on_least.values())[0]
                    print(f"answer for {input_string} is {timestamp+offset_of_least}")
                    return timestamp+offset_of_least

assert find_timestamp('17,x,13,19')==3417
assert find_timestamp("67,7,59,61")== 754018
assert find_timestamp("67,x,7,59,61")==779210
assert find_timestamp("67,7,x,59,61")== 1261476
assert find_timestamp("1789,37,47,1889")==1202161486
print(find_timestamp(full_input))