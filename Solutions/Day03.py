# solution to http://adventofcode.com/2017/day/3

import math

# calclulates Manhattan distance from any given number to the origin square of the first grid
# returns distance (int)
# rank: 350
def findDistance(number):
	distance = 0
	sideLength = 1
	while (sideLength*sideLength < number):
		sideLength += 2
	# add radial distance
	distance = math.ceil((sideLength + 1)/ 2)
	squareArea = sideLength*sideLength
	squarePerimeter = 4*sideLength
	diff = squareArea - number
	while (diff > sideLength):
		diff -= sideLength
	# add perpendicular distance
	distance += abs(diff - math.floor(sideLength / 2) - 1)
	return distance
	
# takes multidimensional grid as argument, along with a row and column coordinate to update.
# the target cell's new value is the sum of all 8 cells around it.  returns new value (int)
def sumSurroundings(grid, row, col):
	return grid[row+1][col+1] + grid[row+1][col] + grid[row+1][col-1] + grid[row][col-1] + grid[row][col+1] + grid[row-1][col+1] + grid[row-1][col] + grid[row-1][col-1]

# finds next number in second grid that is larger than the supplied target number
# uses 100x100 grid initialized to all 0's to begin with.  a really large number might break it
# returns next largest number (int)
def findLargerNumber(target):
	# initialize grid
	grid = []
	for i in range(0, 101):
		grid.append([])
		for j in range(0, 101):
			grid[i].append(0)
	# set middle of grid to 1
	currentRow = 50
	currentCol = 50
	grid[currentRow][currentCol] = 1
	# length of side of current square
	sideLength = 1
	while (sideLength < 100):
		# start square by moving right
		sideLength += 2
		currentCol += 1
		grid[currentRow][currentCol] = sumSurroundings(grid, currentRow, currentCol)
		if grid[currentRow][currentCol] > target:
			return grid[currentRow][currentCol]
		# move upwards until reaching the corner (side length - 2)
		for i in range(0, sideLength - 2):
			currentRow -= 1
			grid[currentRow][currentCol] = sumSurroundings(grid, currentRow, currentCol)
			if grid[currentRow][currentCol] > target:
				return grid[currentRow][currentCol]
		# move left until reaching the corner (side length - 1)
		for i in range(0, sideLength - 1):
			currentCol -= 1
			grid[currentRow][currentCol] = sumSurroundings(grid, currentRow, currentCol)
			if grid[currentRow][currentCol] > target:
				return grid[currentRow][currentCol]
		# move down until reaching the corner (side length - 1)
		for i in range(0, sideLength - 1):
			currentRow += 1
			grid[currentRow][currentCol] = sumSurroundings(grid, currentRow, currentCol)
			if grid[currentRow][currentCol] > target:
				return grid[currentRow][currentCol]
		# move right until reaching the corner, which is the end of the square (side length - 1)
		for i in range(0, sideLength - 1):
			currentCol += 1
			grid[currentRow][currentCol] = sumSurroundings(grid, currentRow, currentCol)
			if grid[currentRow][currentCol] > target:
				return grid[currentRow][currentCol]
	print("Number too large!")
	return -1

if __name__ == "__main__":
	input = 368078
	
	answer1 = findDistance(input)
	print("Distance: " + str(answer1))
	answer2 = findLargerNumber(input)
	print("Next number: " + str(answer2))
	