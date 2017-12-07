# solution to http://adventofcode.com/2017/day/6

# given unparsed list (direct result of reading file), parses into this format:
# list of programs, each with a name, weight, and possible children [ [(string), (int), [(string)]] ]
def parseProgs(progStringList):
	progList = []
	for prog in progStringList:
		newEntry = []
		newEntry.append(prog[0]) # program name
		newEntry.append(int(prog[1][1:-1])) # program weight
		# if there are no programs directly above this one, move to the next
		if len(prog) <= 2:
			progList.append(newEntry)
			continue
		# iterate through all programs directly above
		higherPrograms = []
		for i in range(3, len(prog)):
			higherPrograms.append(prog[i].replace(",", "")) # strip ending comma
		newEntry.append(higherPrograms)
		progList.append(newEntry)
	return progList

# given the name of a program (string), get *all* the corresponding program data from the list
def findProg(progName, progInfo):
	for prog in progInfo:
		if progName == prog[0]:
			return prog
	raise ValueError("Program with name " + progName + " not found")
	return

# given a parsed list of program information, returns the root of the tree
# returns entire program as list of name, weight, and children [(string), (int), [(string)]]
def getParentProgram(progName, progInfo):
	for prog in progInfo:
		if len(prog) <= 2:
			continue
		if progName in prog[2]:
			bottomMost = getParentProgram(prog[0], progInfo)
			return bottomMost
	return findProg(progName, progInfo)

# okay so this one is a little bit hacky but bear with me.
# basically, it doesn't return anything, but it prints out all the needed information.
# once it finds the information, it throws a TypeError exception.  handle that
# and we are good to go.
# rank: 569
def balanceWeight(balanceProg, progInfo):
	progWeight = balanceProg[1]
	# if the program we are looking at has no children, just return its weight
	if len(balanceProg) <= 2:
		return progWeight
	# otherwise, we need to see if the weights balance
	stackWeights = []
	for childName in balanceProg[2]:
		childProg = findProg(childName, progInfo)
		stackWeights.append(balanceWeight(childProg, progInfo))

	# find an anomalous weight, if one exists
	if (len(set(stackWeights)) > 1):
		stackIndex = stackWeights.index(max(stackWeights)) # max works because the anomaly is too heavy
		nextProgName = balanceProg[2][stackIndex]
		nextProg = findProg(nextProgName, progInfo)
		diff = max(stackWeights) - min(stackWeights)
		neededWeight = nextProg[1] - diff # again, subtracting works because the anomaly is too heavy
		print("Anomalous weight found in program: " + nextProgName)
		print("Current weight: " + str(nextProg[1]) + " - required weight: " + str(neededWeight))
		balanceWeight(nextProg, progInfo)
	else:
		return sum(stackWeights) + progWeight
		
if __name__ == "__main__":
	# read file into spreadsheet as list of lists of string
	unparsedList = []
	with open('Day07Input.txt', 'r') as myfile:
		for prog in myfile:
			unparsedList.append(prog.strip().split())
	# print(str(progStringList))
	progList = parseProgs(unparsedList)
	# print(str(progList))
	parent = getParentProgram(progList[0][0], progList)
	print("Bottom-most program name: " + str(parent[0]))
	# error handling that is mentioned in comments for balanceWeight function
	try:
		balanceWeight(parent, progList)
	except TypeError:
		pass