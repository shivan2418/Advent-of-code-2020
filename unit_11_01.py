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


class Seat:
    seats= {k:[] for k in range(len(small_sample.split('\n')[0]))}
    all_seats = []

    def __init__(self,x,y,status):
        self.x =x
        self.y = y
        self.pos = (x,y)
        self.status=status
        self.pending_status_change=None

    def __repr__(self):
        return self.status

    def __str__(self):
        return f"{self.pos} {self.status}"

    @classmethod
    def print_overview_map(cls):
        '''Prints an overview map'''
        for s in Seat.seats.values():
            print(f'{" ".join([a.status for a in s])}')
        print('')

    @classmethod
    def overview_map(self):
        return "".join([s.status for s in self.all_seats])

    def apply_status_change(self):
        if self.pending_status_change is not None:
            self.status = self.pending_status_change
            self.pending_status_change=None

    def get_adjacent_seats(self):
        adjacent_positions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
        # filter away pos at the edge
        adjacent_positions = [(x,y) for x,y in adjacent_positions if self.x+x>=0 and self.y+y>=0]

        ad_seats = []
        for pos in adjacent_positions:
            ad_seats.append(Seat.get_seat_at_pos(pos[0],pos[1]))
        return [s for s in ad_seats if s]

    @classmethod
    def get_seat_at_pos(cls,x,y):
        try:
            return Seat.seats[x][y]
        except IndexError:
            return None
        except KeyError:
            return None

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

    @classmethod
    def run_round(cls):
        # get if anything will change on any of the seats
        for seat in cls.all_seats:
            seat.pending_status_change = seat.get_status_change()

        for seat in cls.all_seats:
            seat.apply_status_change()

x_rows = small_sample.split('\n')

# setup
for x, col in enumerate(x_rows):
    for y, seat in enumerate(col):
        s = Seat(x, y, seat)
        Seat.seats[x].append(s)
        Seat.all_seats.extend([s])

counter=0
round_maps={}
Seat.print_overview_map()

print(f'{counter = }')
round_maps[counter]=Seat.overview_map()
Seat.run_round()
Seat.print_overview_map()



counter+=1
print(f'{counter = }')
Seat.run_round()
Seat.print_overview_map()

round_maps[counter]=Seat.overview_map()


while True:
    counter += 1
    print(f'{counter = }')
    Seat.run_round()
    round_maps[counter] = Seat.overview_map()

    if round_maps[counter]==round_maps[counter-1]:
        Seat.print_overview_map()
        break
