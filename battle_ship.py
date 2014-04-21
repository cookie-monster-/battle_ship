import sys

gGrid = [[]]

def Usage():
	print "python battle_ship.py [grid dimension]"
	print "python battle_ship.py 10"

def DisplayBoard():
	for row in gGrid:
		print ' '.join(map(str, row))
	print ''

def PopulateGrid(grid_dimension):
	for row_index in range(grid_dimension):
		gGrid.append([])
		for cell_index in range(grid_dimension):
			gGrid[-1].append(0)
	DisplayBoard()

def main():
	if len(sys.argv) != 2:
		Usage()
	
	source_file = sys.argv[0]
	grid_dimension = sys.argv[1]
	
	PopulateGrid(int(grid_dimension))

if __name__ == "__main__":
	main()
