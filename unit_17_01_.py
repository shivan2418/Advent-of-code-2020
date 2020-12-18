input = '''.#.
..#
###'''

def get_adjacent_active(base,matrix):


    coordinates = []
    for mod in [1, -1]:
        for pos in range(3):
            new_b = list(base)
            new_b[pos] += mod
            coordinates.append(tuple(new_b))

    num_actives = 0
    for cor in coordinates:
        try:
            if matrix[cor]=='#':
                num_actives+=1
        except KeyError:
            pass
    return num_actives


def setup(input):
    matrix = {}
    z=0
    input = input.split('\n')
    for y,y_let in enumerate(input):
        for x,x_let in enumerate(y_let):
           matrix[(x,y,z)]=x_let

    return matrix

matrix = setup(input)

for round in range(6):

    pending_changes = []

    for pos in matrix.keys():


        num_active = get_adjacent_active(pos,matrix)
        try:
            active = matrix[pos]=='#'
        except KeyError:
            active = False

        if active and num_active in [2,3]:
            pass
        elif active and num_active not in [2,3]:
            pending_changes.append(  (pos,'.') )

        elif not active and num_active == 3:
            pending_changes.append((pos, '#'))

        elif not active and num_active != 3:
            pass
        else:
            raise("Something wrong")

    else:
        # apply pending changes
        for pos,new_value in pending_changes:
            matrix[pos]=new_value