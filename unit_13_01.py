small_input='''939
7,13,x,x,59,x,31,19'''
full_input = '''1000052
23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,19,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41'''

departure_time = int(full_input.split('\n')[0])
bus_schedules_time = full_input.split('\n')[-1].split(',')
bus_schedules_time = [int(n) for n in bus_schedules_time if n!='x']

dep_dict = {bus:[n for n in range(0,departure_time+bus,bus)][-1] for bus in bus_schedules_time}

waits = [value for key,value in dep_dict.items()]
wait_time = min(waits)-departure_time
bus_id = [key for key,value in dep_dict.items() if value==min(waits)][0]

print(f"Bus:{bus_id} Wait time {wait_time}")
print(bus_id*wait_time)