from functools import lru_cache
f = open("day_11_2.txt")
input_data = f.read()
x_rows = input_data.split('\n')


def line_generator(delta_x,delta_y):
    x=0
    y=0
    while True:
        yield (x+delta_x,y+delta_y)

class Seat:
    seats= {k:[] for k in range(len(input_data.split('\n')[0]))}
    all_seats = []
    all_seats_dict={}

    def __init__(self,x,y,status):
        self.x =x
        self.y = y
        self.pos = (x,y)
        self.status=status
        self.pending_status_change=None
        self.seats_visible_in_direction = None

    def __repr__(self):
        return self.status

    def __str__(self):
        return f"{self.pos} {self.status}"

    @classmethod
    def print_overview_map(cls):
        '''Prints an overview map'''
        row_len = len(x_rows[0])
        output = ""
        for seat in Seat.all_seats:
            output = "".join([output,seat.status])
            if len(output)==row_len:
                print(output)
                output=""
        print('')

    @classmethod
    def overview_map(self):
        return "".join([s.status for s in self.all_seats])

    def apply_status_change(self):
        if self.pending_status_change is not None:
            self.status = self.pending_status_change
            self.pending_status_change=None

    def get_visible_seats(self):
        if self.seats_visible_in_direction is None:
            # the eight directions
            line_slopes = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

            seats_visible_in_direction = {s:[] for s in line_slopes}

            for slope in seats_visible_in_direction.keys():
                x_slope, y_slope = slope
                line = line_generator(x_slope,y_slope)

                start_x,start_y = self.pos
                d_x, d_y = next(line)
                x = start_x+d_x
                y = start_y+d_y
                visible_seat = Seat.get_seat_at_pos(x,y)
                seats_visible_in_direction[slope].append(visible_seat)
                while visible_seat is not None:
                    d_x, d_y = next(line)
                    x += d_x
                    y += d_y
                    visible_seat = Seat.get_seat_at_pos(x,y)
                    seats_visible_in_direction[slope].append(visible_seat)


            self.seats_visible_in_direction = seats_visible_in_direction
            return seats_visible_in_direction
        else:
            return self.seats_visible_in_direction

    def get_first_visible_seats(self):
        directions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

        visible_seats = self.get_visible_seats()

        first_seen_seats = []

        for d in directions:
            seats_in_this_direction = visible_seats[d]

            for seat in seats_in_this_direction:
                if seat is None: # reached the end, fill in None for good measure
                    break
                if seat.status =='.': # look over floor
                    continue
                if seat.status in ['L','#']:
                    first_seen_seats.append(seat)
                    break

        return first_seen_seats

    def get_num_occupied_visible_seats(self):
        visible = [s.status for s in self.get_first_visible_seats()]
        return visible.count('#')

    @classmethod
    def get_seat_at_pos(cls,x,y):
        try:
            return Seat.all_seats_dict[(x,y)]
        except IndexError:
            return None
        except KeyError:
            return None

    @classmethod
    def get_total_num_occupied_seats(cls):
        return len([s for s in Seat.all_seats if s.status=='#'])

    def get_status_change_visible(self):
        if self.status == '.':  # floor never changes
            return None
        visible_occupied = self.get_num_occupied_visible_seats()

        if self.status == 'L':
            if visible_occupied == 0:
                return '#'
        elif self.status == '#':
            if visible_occupied >= 5:
                return 'L'

        return None

    @classmethod
    def run_round_visible(cls):
        # get if anything will change on any of the seats
        for seat in cls.all_seats:
            seat.pending_status_change = seat.get_status_change_visible()

        for seat in cls.all_seats:
            seat.apply_status_change()


# setup
for y, col in enumerate(x_rows):
    for x, status in enumerate(col):
        s = Seat(x, y, status)
        Seat.all_seats.append(s)
        Seat.all_seats_dict[s.pos]=s

# print the status before start
counter=0
round_maps={}
Seat.print_overview_map()

# save the round 0 map
round_maps[counter]=Seat.overview_map()
Seat.run_round_visible()
Seat.print_overview_map()

# run one round
counter+=1
Seat.run_round_visible()
Seat.print_overview_map()
round_maps[counter]=Seat.overview_map()

# run until the new map generated equal the one generated in the previoud round
while True:
    counter += 1
    Seat.run_round_visible()
    round_maps[counter] = Seat.overview_map()

    if round_maps[counter]==round_maps[counter-1]:
        Seat.print_overview_map()
        print(Seat.get_total_num_occupied_seats())
        break
