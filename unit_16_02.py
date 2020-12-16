from collections import defaultdict, Counter

with open('day_16.txt','r') as f:
    full_input = f.read()

sample_input = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

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

def valid_for_all_field(value,valid_ranges):
    return all([value in v_range for v_range in valid_ranges])

def get_invalid_tickets(input):

    content = input.split('\n')

    rules = []
    my_ticket = []
    nearby_tickets=[]
    current_list = rules
    append_list_generator = (l for l in [my_ticket,nearby_tickets])

    for ticket in content:
        if ticket == "":
            current_list = next(append_list_generator)
        else:
            current_list.append(ticket)

    my_ticket = [int(n) for n in my_ticket[1].split(',')]

    nearby_tickets = nearby_tickets[1:]
    nearby_tickets = [[int(l) for l in ticket.split(',')] for ticket in nearby_tickets]

    valid_ranges = []
    valid_tickets = []
    for rule in rules:
        valid_ranges.extend(parse_rule(rule))

    for ticket in nearby_tickets:
        for value in ticket:
            if not valid_for_any_field(value,valid_ranges):
                break
        else:
            valid_tickets.append(ticket)

    rules_dict = {}
    rules_pos = defaultdict(set,{})
    for rule in rules:
        category = rule.split(':')[0]
        ranges = parse_rule(rule)
        ranges_set = set()
        for ran in ranges:
            for r in ran:
                ranges_set.add(r)
        rules_dict[category]= ranges_set

    for rule,valid_numbers in rules_dict.items():
        for col in range(len(valid_tickets[0])):
            vertical_values = [int(item[col]) for item in valid_tickets]

            if all([v in valid_numbers for v in vertical_values]):
                rules_pos[rule].add(col)


    final_pos = get_final_positions(rules_pos)

    departure_values = [v for k,v in final_pos.items() if 'departure' in k]
    final_values = [my_ticket[index] for index in departure_values]
    i = 1
    for v in final_values:
        i*=v

    return i

def get_final_positions(rules_pos,return_dict=None)->dict:
    if return_dict is None:
        return_dict = {}

    # guard against being last item
    if len(rules_pos)==1:
        remaining_key,remaining_values = list(rules_pos.items())[0]
        for value in remaining_values:
            if value not in return_dict.values():
                return_dict.update({remaining_key:value})
                return return_dict

    # fill in all that have only one options
    only_option = {k:v for k,v in rules_pos.items() if len(v)==1}
    if len(only_option)>0:
        for category,possible_pos in only_option.items():
            value = possible_pos.pop()
            return_dict.update({category:value})
            rules_pos.pop(category)
        for values in rules_pos.values():
            values.remove(value)

        return get_final_positions(rules_pos,return_dict)

    for category,possible_pos in rules_pos.items():
        other_pos = {k:v for k,v in rules_pos.items() if k!=category}
        for pos in other_pos.values():
            if len(possible_pos-pos)==1:
                value = set(possible_pos-pos).pop()
                return_dict.update({category: value})
                rules_pos.pop(category)
                return get_final_positions(rules_pos, return_dict)

print(get_invalid_tickets(full_input))