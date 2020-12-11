small_sample = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

big_sample='''LLLLLLLLLLLLLL...LLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.L.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL..LLLLLLLLL.LLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLL.LL
LLLLLL.LLLLLLLL.L.LL.LLLLLLLLLLLL.L.L.LL.LLLLLLLLL.LLLLLL.L.LLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
L.LLLL.LLLLLLLL.LLLL.LLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLL.LLLLL.LL.LLLLLLLLLLL
LLL.LL.LLLLLLLLLLLLL..LLLL.LLLLLLLL.L.LLL.LL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
L.....LLLLL.LL.L.L..L..L.L..LL...LLLLL.L...L..LLL.L.L..L...LLL.LL.L..LL...L......L.L.L.L.LLLLL....
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLL.LLLL.LLLLLLLLLL.LL..L.LLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLL.L.LLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.L.L.LLLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLL.LLL
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLL.L.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
.L.L...L.LL....L.......L...LLL.LL....L.LL.LLL...L........L..L.....L........L.LLL..L..LL.LL........
LLLLLL.LLLLLLLL.LLLL.LLLLLLLL...LLLLL.LLLLLL.LLLLL..LLLLLLLL.LLLLLLLL.L.LLLLL.LLLLL.LLLLLLLLLLLL.L
LLLLLL.LLL.LLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLL
LLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLL.LLLLLL.LLLL..LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.L.LLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLL.LLL
LL.LLL..LLLLLLLLLL.L.LLLLLLLLL.LLLL.L.LLLLLL.LLLLL..LLLLLLLLLLLLLLLLL.LLLLLLL.L.LLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLL..LLL.L.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLL.LLLLLLLLLLLLLL
.L.........LL.LL..L..LLLL...L.........L.LLL..L....L....LLL.....L..L.L..L........LL..LL..L.....L...
L.LLLL.LLLLLLLL.LLL..LLLLLLLLLLL.LLL..LLLLLL.LLLLL.LLLLLLLL.L..LLLLLL.LLLLLLLLL.LLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.
LLLLLLLLL.LLLLL..LLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLL.LLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLL.LLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLLL
LLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLL.LL.LLLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLL.L.LLLLL.LL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
.....L....L.L...LL...LL..L.LL.....L............LL...LL..LL.L.L......LL........L.L..L....L....L..L.
L.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL..LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.L.LLLLLLLLLLLL
L.LLLL..LLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLL..LLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LL.LLLLLLLL.LLLLLLLL.LLLLLLLLLL.LLL.LLLLLLLLLLLLLL
LLLLLL.LLLLL.LLLLLLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLL
LLLLLLLL.LLLLLL.LLLL.LLLL.LLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLL.L.LLLLL.LLLLLLL.LLLLLL
LLLLL..LLLLLLLLLLLLLLLLLLLLL.L.LLLLLL.LLL.LL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
L..L.L.L.L........L...L.L..LL....L.....L.L......L..L........LL........L......LL.LLL.L..LL...LL...L
LLLLLL.LLLLLLLL.LLLL.LLLL.LLLL.LLLLLLLLL.LLLLLLLLL.LLLLL.LL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LL.L.LLLLLLLLLL.LLLL.LLL.LLLLLLLLLLLL.LLLLLL.LLLLL..LLLLLLL.LLLLLLLLL.LLL.LLL.LLLLLLLLLLLLLLLLLLL.
LLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLL.LLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLL.LL.LL.LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
...LL.LL.L..LL..L.LLL........L...L.......L...L..L.LL.L.......L....L...L.....LLL.L..L.L..L.L..L....
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLL.L.LLLLLLLL..LLLLLLL.LLLLL.LLLLL.LLLLLLLL
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.L.LLLL.LLLLLL.L.LLLLLLLLLLLLLLLLLLLL.L.LLLLL.L.LLLLLLLLL.LLLLLLLLLL
L..LLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLL.LLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLL..LLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
.LLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
L.LLLL.LLLLLLLL.LLLL.LLLLLLL.L.LLLLL..LLLLLL.LLLLL.LLLLLLLLLL.LLLLLLL.LL.LL.L.LLLLL.LLLLLLLLLLLLLL
LL.L...L.........L..L...LLL......L......L...L..L.L..LL..L.LLL.LL..L.LL..L.L.LL.L.L..LL..........L.
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL
LL.LLL..LLLLLLLLLLLL..LLLLLLLL.LLLLLL.L.LLLL.LLLLLLLLLLLLLL.L.LLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LL.LLL.LLLLLL.LLLLL.L.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLL
LLLLL...LLLLLLLLLLLLLLLLLLLLLL.LL.LLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLL.LLLLLLLL
LLLLLLLLLLLLLLL..LLL.LLLLLLLLL.LLLLLL.LLLLLLLLLLL..LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLL.LLLLL..LLLLL.LLLLLLLL.L.LLLLL.L.LLLLLLL.LLLL..LLLLLLLLLLLLLL
LLLLLL.LL.LL.LL.LLLL.LLLLLLLLL.LLL.LL.LLL.LL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
L.LLLL.L.LLLLLL.LLLLLLLLLLLLLL.L.LLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLL.LL..LLLLL.LLLLLLLLLLLL.L
..L.....LLLL..L..L......LL.L.......L..LLL..L..L..LL.LLL....L..L.L..L...L.LL..L...L.L.......L......
LLLLLL.LLLLLLLL..L.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLL.LL.LLLLLL.LLLLLLL.LL.LL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLLL.LLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLL.L.LLLL.LL.LLLLL.LLLL..LLLLLLLL.LLLLLLLLL.LLLLLLL.L.LLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL..LLLLL.LLL.LLLLLL.L.L
LLL.LLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLL.LLLLLLL.LLLL.LLLLLLLL.LLL.LL.LL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLL..LLLLLLLL.LL.LLLLLLLLLLL.LLLLLL.LLLLLL.L.LLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
L..L...L.L.L....L....L.LLLL.L.....L..LL...L...L..LLL.L......LL...L..LLL..L.L..L....L.L.L...L..LL.L
LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL..LLLL.LL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LL
LLLLLLLLLLLLLLL.LLLL.LLL.LLL.LLLLLLLLLLLLLLL.LLLLL.LLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLL.L.L
LLLLLL.LLL.LLLLL.LLL.L.LLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLL.LL.LLL..LLLLLLL.LLLLL.LLLLL.LLLLLLLL
LLLLLL.LLLLLLLLLLLLL.LLLL.L.L..LLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLL.LLLLLL.LLLLLLLLLL.LL.LLLLLL.LL.LLLL.LLLLL.LLLLLLLL.LLL.L
.LLL.LLLLLLLL.L.LLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLL.LLLLLLL..LLLLLL.LLLL.LLLLLLLLLLLLLLL
LL.LLL.L.LL.LLLL.....L...LL..L....LL.LLL.....L..L..L..L.............L.L.....L......LLL.L.....L.LL.
LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLL
LLLLLL.L.LLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLL
LLLLLL.L.LLLLLL.LLLL.L.LLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLLL
LLL.LLLLLLLL.LL.LLLL.LLLLLLLLL.LLLLLLLL..LLL.LLLLL.LLL.LLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLL..LLLLLLLLLLLL.LLLLLLLLLLLLLL.LLL..LLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLL
.L....L...L.....LL.L..LL.L.L..LLL..L...L......LL..L..L.LL..L..LLLL..L...LLL.L.LLL.L.L...LL..L.L...
LLLLLL..LLLLLLLL.L.LLLLLLL.LLL..LLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLL.LLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LL.L.LLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLLLLLLLLLLLL.LLLLLL.LLLLLL.LL...LLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.
LLLL.L.LLLLLLLLLLL.L.LLLLL..LL.LLL.LL.LL.LLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLL.LLLLLLLLLL.LL.LLLLL.LLLLLLLL.LLLLLLLLLLLL..LLL.LLLLL.LLLLLLLLLLL.LL
L.L.L.L.LL...L....L.L.L...L.L.....L....LL..L.L....LL..LL..L.......................L.L...L..L..L...
LLLLLL.LLLLLLLL.LLLLLLLLLLLL.L.LLLLLLLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLL
LLLLLL.LL.LLLLL.LLL.LLL.LLLLL..LLL.LL.LLLLLL.LLLL..LLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL
.LLLLL.LLLLLLLL.L.LL.LLLLL.LL.LLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLL..LLLLL.LL.LLLLLL..LLLLL.LLLL.LLLLLLL.L.LLLLLLLLL.LLLLLLLLLLLLL..LLLLLLLLLLLLL
LLLLLLLLLLLLL.LLLLLL..LLLLLLLL.LLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLL.LL.LLLLLL.LLLL
LLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLL..LLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLL.LLLLLLLL.LLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLL..L.LLLLLLLLL.LLLL.LL.L..LL.LLLLLLLLLLLLLL'''

from functools import lru_cache
from elutils.decorators import timeit

def line_generator(delta_x,delta_y):
    x=0
    y=0
    while True:
        yield (x+delta_x,y+delta_y)

class Seat:
    seats= {k:[] for k in range(len(small_sample.split('\n')[0]))}
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

    @timeit
    @lru_cache(maxsize=12)
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


    @lru_cache()
    @timeit
    def get_adjacent_seats(self):
        adjacent_positions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        possible_adjacent = [(self.x+x,self.y+y) for x,y in adjacent_positions]
        ad_seats = []
        for pos in possible_adjacent:
            try:
                s = Seat.all_seats_dict[pos]
                ad_seats.append(s)
            except KeyError:
                pass
        return ad_seats

    @timeit
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


    def get_num_occupied_adjacent_seats(self):
        ad_seats = self.get_adjacent_seats()
        occupied_seats = [s.status for s in ad_seats].count('#')
        return occupied_seats

    def get_status_change(self):
        if self.status=='.': # floor never changes
            return None
        adjacent_occupied = self.get_num_occupied_adjacent_seats()

        if self.status=='L':
            if adjacent_occupied==0:
                return '#'
        elif self.status=='#':
            if adjacent_occupied>=4:
                return 'L'

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
    @timeit
    def run_round(cls):
        # get if anything will change on any of the seats
        for seat in cls.all_seats:
            seat.pending_status_change = seat.get_status_change()

        for seat in cls.all_seats:
            seat.apply_status_change()

    @classmethod
    def run_round_visible(cls):
        # get if anything will change on any of the seats
        for seat in cls.all_seats:
            seat.pending_status_change = seat.get_status_change_visible()

        for seat in cls.all_seats:
            seat.apply_status_change()

# set what data to use here
x_rows = big_sample.split('\n')

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
