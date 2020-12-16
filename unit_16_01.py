with open('day_16.txt','r') as f:
    full_input = f.read()

sample_input = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''


def parse_rule(string):
    ranges=[]

    string = string.split(":")[-1]
    first,second = string.split("or")
    for s in [first,second]:
        r_low,r_high = s.split("-")
        ranges.append(  range(int(r_low),int(r_high)+1) )

    return ranges

def valid_for_any_field(value,valid_ranges):
    return any([value in v_range for v_range in valid_ranges])

def get_invalid_tickets(input):

    content = input.split('\n')

    rules = []
    my_ticket = []
    nearby_tickets=[]
    current_list = rules
    append_list_generator = (l for l in [my_ticket,nearby_tickets])

    for line in content:
        if line=="":
            current_list = next(append_list_generator)
        else:
            current_list.append(line)

    my_ticket = my_ticket[1:]
    nearby_tickets = nearby_tickets[1:]

    valid_ranges = []
    for rule in rules:
        valid_ranges.extend(parse_rule(rule))

    invalid_values = []

    for line in nearby_tickets:
        for value in line.split(','):
            value = int(value)
            if not valid_for_any_field(value,valid_ranges):
                invalid_values.append(value)


    print(sum(invalid_values))
    return sum(invalid_values)

assert get_invalid_tickets(sample_input) == 71

get_invalid_tickets(full_input)