# solution to http://adventofcode.com/2017/day/14

import Day10
import binascii

# popcount function: returns the number of on bits in a binary number
# from https://www.expobrain.net/2013/07/29/hamming-weights-python-implementation/
def popcount(x):
    x -= (x >> 1) & 0x5555555555555555
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    return ((x * 0x0101010101010101) & 0xffffffffffffffff ) >> 56

# given a list of bytearrays, return a list of lists of bits
def getBitArray(hashList):
	# turn list of bytearray hashes into list of int hashes
	hashVals = []
	for i in range(0, 128):
		hashVals.append(int(binascii.hexlify(hashes[i]), 16))
	# turn list of int hashes into list of lists of bits
	hashBits = []
	for i in range(0, 128):
		hashBits.append([])
		for j in range(0, 128):
			bitMask = mask = 2**(127 - j)
			testBit = bitMask & hashVals[i]
			if testBit != 0:
				hashBits[i].append(1)
			else:
				hashBits[i].append(0)
	return hashBits

# function to traverse an entire region of 1's in a given 2d array of 0's and 1's
# updates "visited" list with ordered tuple (row, col)
# returns nothing - only purpose is to update "visited" list
def getRegion(hashBits, row, col, visited):
	# test bit to the left, if it exists
	if col > 0:
		if hashBits[row][col-1] != 0 and (row, col-1) not in visited:
			visited.append((row, col-1))
			getRegion(hashBits, row, col-1, visited)
	# test bit to the right, if it exists
	if col < 127:
		if hashBits[row][col+1] != 0 and (row, col+1) not in visited:
			visited.append((row, col+1))
			getRegion(hashBits, row, col+1, visited)
	# test bit above, if it exists
	if row > 0:
		if hashBits[row-1][col] != 0 and (row-1, col) not in visited:
			visited.append((row-1, col))
			getRegion(hashBits, row-1, col, visited)
	# test bit below, if it exists
	if row < 127:
		if hashBits[row+1][col] != 0 and (row+1, col) not in visited:
			visited.append((row+1, col))
			getRegion(hashBits, row+1, col, visited)
	return

# get the number of regions of 1's in a given 2d array of 0's and 1's (list of lists of int)
# returns number of regions (int)
def getNumRegions(hashBits):
	visited = []
	regions = 0
	# test every bit for the start of a new region
	for row in range(0, 128):
		for col in range(0, 128):
			if hashBits[row][col] != 0 and (row, col) not in visited:
				# mark bit as visited and traverse region
				regions += 1
				visited.append((row, col))
				getRegion(hashBits, row, col, visited)
	return regions
	
if __name__ == "__main__":
	# part 1 - get number of 'on' bits in an array of 128 knot hashes
	# rank: 105
	input = "stpzcrnm"
	hashes = []
	print("Finding number of on bits...")
	for i in range(0, 128):
		rowName = input + "-" + str(i)
		inputBytes = bytearray(rowName, "ascii")
		hashes.append(Day10.getKnotHash(inputBytes))
	onBits = 0
	for i in range(0, 128):
		for byte in hashes[i]:
			onBits += popcount(byte)
	print("On bits: " + str(onBits))
	
	# part 2: get number of regions of 'on' bits in the array
	# rank: 304
	print("Finding number of regions...")
	hashBits = getBitArray(hashes)
	numRegions = getNumRegions(hashBits)
	print("Regions: " + str(numRegions))