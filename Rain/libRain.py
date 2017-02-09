import sys

try:
    FILENAME = sys.argv[1]
except IndexError:
    print ("Input file required.")
    sys.exit(1)

def get_tests_from_file(file):
	with open(file) as f:
		content = f.readlines()

	try:
		TEST_COUNT = int(content[0])
		del content[0]
	except IndexError:
		print ("Input file invalid.")

	tests = []

	for t in range (0, TEST_COUNT):
		testDimensions = content[0].split()
		test_rows = int(testDimensions[0])
		test_columns = int(testDimensions[1])

		test_map = []

		for line in content[1:test_rows + 1]:
			test_map.append(line.rstrip().split())

		test_tuple = t, test_rows, test_columns, test_map
		tests.append(test_tuple)


		del content[0:test_rows + 1]

	return tests

tests = get_tests_from_file(FILENAME)

print(tests)

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
            if graph[up[0]][up[1]] < target_height:
                lower_matches.append(graph[up[0]][up[1]])   # Append if smaller
        except IndexError:
            pass
