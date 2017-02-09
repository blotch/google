GRAPH = [[5, 5, 5, 1],
         [5, 2, 2, 5],
         [5, 5, 5, 5],
         [5, 5, 5, 8]]

COORD = [0, 0]




'''
    fix the x / y coordinate mismatch!


'''






print(GRAPH[COORD[0]][COORD[1]])

'''
    get_lower_cordinates() - This function is used for determining which
    cells (connected via edges) contain lower elevations than the target
    cell. It does not include oceans.

    This function expects both a graph (in the form of a two-dimensional array)
    and [x, y] coordinates in the form of an array.

    This function returns an array of arrays including the x,y coordinates
    of adjacent cells with a lower water level.
'''
def get_lower_coordinates(graph, coordinates):
    lower_matches = []
    y = coordinates[0]
    x = coordinates[1]
    target_height = graph[first][second]

    # Calculate offsets
    up = [y-1][x]
    right = [y][x+1]
    down = [y-1][x]
    left = [y][x-1]

    # Check up
    if up[0] >= 0 and up[1] >= 0: # Verify we aren't off the grid
        try:
            if graph[up[0][up[1]] < target_height:
                lower_matches.append(graph[up[0]][up[1]])   # Append if smaller
        except IndexError:
            pass

    # Check right
    if right[0] >= 0 and right[1] >= 0: # Verify we aren't off the grid
        try:
            if graph[right[0][right[1]] < target_height:
                lower_matched.append([right[0]
                    
    # Check bottom

    # Check left


    pass
    
