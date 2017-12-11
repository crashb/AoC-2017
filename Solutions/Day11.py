# solution to http://adventofcode.com/2017/day/11

# part 1: follow a path and find the shortest distance to its destination.
# takes a list of directional strings: "n", "s", "ne", "sw", "nw", and "se".
# the y-axis runs from n-s, while the x-axis runs from ne-sw.  there is a third
# axis, the z-axis, which runs from nw-se.  interestingly, x + y + z = 0 for
# the coordinates of any given tile.
# very helpful: http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
# returns minimum distance (int)
# rank: 297
def followPath(dirList):
	x = 0
	y = 0
	for dir in dirList:
		if dir == "n":
			y += 1
		elif dir == "s":
			y -= 1
		elif dir == "ne":
			x += 1
		elif dir == "sw":
			x -= 1
		elif dir == "nw":
			y += 1
			x -= 1
		elif dir == "se":
			y -= 1
			x += 1
	# now that we have x and y coordinates, get z coordinate using x + y + z = 0 property
	z = 0 - x - y
	# print("x, y, z: " + str(x) + "," + str(y) + "," + str(z))
	# we might get negative values for x, y, z, so make sure to get absolute val of each
	d = max(abs(x), abs(y), abs(z))
	return d

# part 2: find the furthest distance a given path (list of strings) strays from the origin.
# just runs the code from part 1 over and over.  not efficient in any way.
# there exists a much more efficient way that only traverses the list once.
# returns maximum distance (int)
def furthestDistance(dirList):
	print("Calculating furthest distance...")
	currentDirs = []
	maxDist = 0
	for i in range(0, len(dirList)):
		currentDirs.append(dirList[i])
		newDist = followPath(currentDirs)
		if newDist > maxDist:
			maxDist = newDist
	return maxDist

if __name__ == "__main__":
	# read input file into list of strings
	with open('Day11Input.txt', 'r') as myfile:
		dirList = myfile.read().strip().split(",")
	# print(str(dirList))
	distance = followPath(dirList)
	print("Shortest distance: " + str(distance))
	farDistance = furthestDistance(dirList)
	print("Furthest distance: " + str(farDistance))