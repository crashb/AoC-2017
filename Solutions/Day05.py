# solution to http://adventofcode.com/2017/day/5

import math

# jumps around an instruction list (list of int)
# returns number of jumps it takes to escape list
# rank: 666
def jump1(instList):
	numJumps = 0
	currentPos = 0
	jumpDistance = 0
	while (True):
		jumpDistance = instList[currentPos]
		instList[currentPos] += 1
		currentPos += jumpDistance
		numJumps += 1
		if currentPos < 0 or currentPos >= len(instList):
			return numJumps
			
# jumps around an instruction list (list of int)
# returns number of jumps it takes to escape list
# rank: 553			
def jump2(instList):
	numJumps = 0
	currentPos = 0
	jumpDistance = 0
	while (True):
		jumpDistance = instList[currentPos]
		if instList[currentPos] >= 3:
			instList[currentPos] -= 1
		else:
			instList[currentPos] += 1
		currentPos += jumpDistance
		numJumps += 1
		if currentPos < 0 or currentPos >= len(instList):
			return numJumps

if __name__ == "__main__":
	# solve problem 1
	instList = []
	with open('Day05Input.txt', 'r') as myfile:
		for inst in myfile:
			instList.append(int(inst.strip()))
	numJumps1 = jump1(instList)
	print("Solution to problem 1: " + str(numJumps1))
	# solve problem 2
	instList = []
	with open('Day05Input.txt', 'r') as myfile:
		for inst in myfile:
			instList.append(int(inst.strip()))
	numJumps2 = jump2(instList)
	print("Solution to problem 2: " + str(numJumps2))
	