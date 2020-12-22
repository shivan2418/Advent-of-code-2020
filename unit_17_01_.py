input = '''.#.
..#
###'''


neighbour_cache = {}


def get_adjacent_coordinates(base):

    try:
        # try to fetch from cache
        coordinates = neighbour_cache[base]
    except KeyError:
        coordinates = []
        for mod in [1, -1]:
            for pos in range(3):
                new_b = list(base)
                new_b[pos] += mod
                coordinates.append(tuple(new_b))
        # save to cache
        neighbour_cache[base]=coordinates

    return coordinates

def get_adjacent_active(base,matrix):

    coordinates = get_adjacent_coordinates(base)
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

#enlarge cube
for round in range(6):

    n_coordinates = []
    [n_coordinates.extend(get_adjacent_coordinates(pos)) for pos in matrix.keys()]
    new_cubes = []
    n_coordinates = list(set(n_coordinates))
    for cor in n_coordinates:
        try:
            value = matrix[cor]
        except KeyError:
            new_cubes.append( (cor,'.')    )

    for pos,value in new_cubes:
        matrix[pos]=value


def advance_round(matrix):
    pending_changes = []

    for pos in matrix.keys():

        num_active = get_adjacent_active(pos, matrix)
        try:
            active = matrix[pos] == '#'
        except KeyError:
            active = False

        if active:
            if num_active in {2,3}:
                pass
            else:
                pending_changes.append((pos, '.'))

        elif not active:
            if num_active ==3:
                pending_changes.append( (pos,'#')  )
            else:
                pass


    # apply pending changes
    for p, new_value in pending_changes:
        matrix[p] = new_value

    matrix_values = list(matrix.values())
    print(f"Num active: {matrix_values.count('#')}")

    return matrix

for round in range(6):
    matrix = advance_round(matrix)

    matrix_values = list(matrix.values())
    print(f"Num active: {matrix_values.count('#')}")
