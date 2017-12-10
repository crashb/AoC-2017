# solution to http://adventofcode.com/2017/day/10

import binascii

# tie knots for part 1
# returns tied list (list of int)
def tieKnots1(circleList, lengthList):
	currentPos = 0
	skipSize = 0
	circleLength = len(circleList)
	
	for length in lengthList:
		# obtain subsection
		newSection = []
		for i in range(0, length):
			circleIndex = (currentPos + i) % circleLength
			newSection.append(circleList[circleIndex])
		# reverse subsection
		newSection.reverse()
		# print("New section: " + str(newSection))
		# apply subsection
		for i in range(0, length):
			circleIndex = (currentPos + i) % circleLength
			circleList[circleIndex] = newSection[i]
			
		currentPos += length + skipSize
		currentPos = currentPos % circleLength
		skipSize += 1
		# print("Tied knot: " + str(circleList))
	return circleList

# tie knots for part 2
# only difference from part 1 is that it accepts parameters for currentPos and skipSize
# returns the following list: [tied list (int of list), currentPos (int), and skipSize (int)]
def tieKnots2(circleList, lengthList, currentPos, skipSize):
	# print("starting at pos " + str(currentPos) + " with skip size " + str(skipSize))
	circleLength = len(circleList)
	
	for length in lengthList:
		# obtain subsection
		newSection = []
		for i in range(0, length):
			circleIndex = (currentPos + i) % circleLength
			newSection.append(circleList[circleIndex])
		# reverse subsection
		newSection.reverse()
		# apply subsection
		for i in range(0, length):
			circleIndex = (currentPos + i) % circleLength
			circleList[circleIndex] = newSection[i]
			
		currentPos += length + skipSize
		currentPos = currentPos % circleLength
		skipSize += 1
		# print("Tied knot: " + str(circleList))
	return [circleList, currentPos, skipSize]

# get dense hash from sparse hash by XOR'ing 16-byte blocks together
# returns dense hash (bytearray)
def getDenseHash(circleList):
	denseHash = bytearray()
	for i in range(0, 256, 16):
		# hash together one block of 16 bytes
		currentByte = 0
		for j in range(0, 16):
			currentByte ^= circleList[i+j]
		denseHash.append(currentByte)
	return denseHash

if __name__ == "__main__":
	# part 1
	# read input file into list of int
	with open('Day10Input.txt', 'r') as myfile:
		lengthListString = myfile.read().strip().split(",")
	lengthList = []
	for item in lengthListString:
		lengthList.append(int(item))
	circleList = list(range(0, 256))
	tiedList = tieKnots1(circleList, lengthList)
	print("Part 1 - Product: " + str(tiedList[0]*tiedList[1]))
	
	# part 2
	# read input file into bytearray
	with open('Day10Input.txt', 'r') as myfile:
		inputBytes = bytearray(myfile.read().strip(), "ascii")
	# add predetermined lengths to end of sequence
	inputBytes.append(17)
	inputBytes.append(31)
	inputBytes.append(73)
	inputBytes.append(47)
	inputBytes.append(23)
	# run 64 rounds of knot-tying, remembering currentPos and skipSize
	currentPos = 0
	skipSize = 0
	for i in range(0, 64):
		result = tieKnots2(circleList, inputBytes, currentPos, skipSize)
		circleList = result[0]
		currentPos = result[1]
		skipSize = result[2]
	# get and print hash
	denseHash = getDenseHash(circleList)
	denseHex = binascii.hexlify(denseHash).decode("ascii")
	print("Part 2 - Dense Hash: " + denseHex)