import sys

try:
	FILENAME = sys.argv[1]

except IndexError:
	print "Input file required."
	sys.exit(1)

def get_tests_from_file(file):
	with open(file) as f:
		content = f.readlines()

	try:
		TEST_COUNT = int(content[0])
		del content[0]
	except IndexError:
		print "Input file invalid."

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
