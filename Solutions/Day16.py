# solution to http://adventofcode.com/2017/day/16

# execute spin move on a list of positions. move syntax: "X"
# returns list of positions
def executeSpin(move, positions):
	moveNum = int(move)
	moved = positions[-moveNum:]
	return moved + positions[:-moveNum]
	
# execute exchange move on a list of positions. move syntax: "1/2"
# returns list of positions
def executeExchange(move, positions):
	switchPos = list(map(int, move.split("/")))
	switch1 = positions[switchPos[0]]
	switch2 = positions[switchPos[1]]
	positions[switchPos[0]] = switch2
	positions[switchPos[1]] = switch1
	return positions
	
# execute partner move on a list of positions. move syntax: "a/b"
# returns list of positions
def executePartner(move, positions):
	switchPos = move.split("/")
	pos1 = positions.index(switchPos[0])
	pos2 = positions.index(switchPos[1])
	positions[pos1] = switchPos[1]
	positions[pos2] = switchPos[0]
	return positions

# execute a list of moves on a list of positions
# returns list of final positions
def executeMoves(moveList, positions):
	for move in moveList:
		# print(positions)
		if move[0] == "s":
			positions = executeSpin(move[1:], positions)
		elif move[0] == "x":
			positions = executeExchange(move[1:], positions)
		elif move[0] == "p":
			positions = executePartner(move[1:], positions)
	return positions
	
# counts the number of times a given dance must be performed to return to
# original position.
# returns int
def getCycleLength(moveList, positions):
	initialPos = list(positions)
	dances = 0
	while(True):
		positions = executeMoves(moveList, positions)
		dances += 1
		if positions == initialPos:
			# print("Returned to initial position!")
			return dances

# performs a lot of the same dance at once
# returns final list of positions
# rank: 564
def manyDances(moveList, positions, numDances):
	cycleLength = getCycleLength(moveList, positions)
	dancesRemaining = numDances % cycleLength
	for i in range(0, dancesRemaining):
		positions = executeMoves(moveList, positions)
	return positions

if __name__ == "__main__":
	with open("Day16Input.txt") as myfile:
		moveList = myfile.read().strip().split(",")
		
	positions = []
	for i in range(0, 16):
		positions.append(chr(97 + i))
		
	result = executeMoves(moveList, positions)
	print("After first dance: " + str(result))
	endPositions = manyDances(moveList, positions, 1000000000)
	print("After billion dances: " + str(endPositions))