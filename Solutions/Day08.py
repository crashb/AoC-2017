# solution to http://adventofcode.com/2017/day/8

# global holding largest value during execution
largestValue = 0

# returns list of dictionaries, each dictionary representing one instruction
def parseInsts(unparsedList):
	parsedInsts = []
	for item in unparsedList:
		newInst = {}
		newInst["name"] = item[0]
		if item[1] == "inc":
			newInst["op"] = 1
		elif item[1] == "dec":
			newInst["op"] = -1
		newInst["val"] = int(item[2])
		newInst["conditionName"] = item[4]
		newInst["conditionOp"] = item[5]
		newInst["conditionVal"] = int(item[6])
		parsedInsts.append(newInst)
	return parsedInsts

# get register names from parsed list and set all values to 0
# returns dictionary: (register name (string): value (int))
def getAllRegisters(parsedList):
	regVals = {}
	for inst in parsedList:
		if inst["name"] not in regVals:
			regVals[inst["name"]] = 0
		if inst["conditionName"] not in regVals:
			regVals[inst["conditionName"]] = 0
	return regVals

# update register value dictionary based on instructions
# returns nothing
def runInsts(instList, regVals):
	global largestValue
	for inst in instList:
	
		# evaluate condition
		valid = False
		if inst["conditionOp"] == "==":
			if regVals[inst["conditionName"]] == inst["conditionVal"]:
				valid = True
		elif inst["conditionOp"] == "<=":
			if regVals[inst["conditionName"]] <= inst["conditionVal"]:
				valid = True
		elif inst["conditionOp"] == "<":
			if regVals[inst["conditionName"]] < inst["conditionVal"]:
				valid = True
		elif inst["conditionOp"] == ">":
			if regVals[inst["conditionName"]] > inst["conditionVal"]:
				valid = True
		elif inst["conditionOp"] == ">=":
			if regVals[inst["conditionName"]] >= inst["conditionVal"]:
				valid = True
		elif inst["conditionOp"] == "!=":
			if regVals[inst["conditionName"]] != inst["conditionVal"]:
				valid = True
		
		if not valid:
			# if the condition is not true, move to the next one
			continue
		else:
			# otherwise, execute the instruction
			regVals[inst["name"]] += inst["op"] * inst["val"]
			# update largest value if necessary
			if regVals[inst["name"]] > largestValue:
				largestValue = regVals[inst["name"]]
	return
		
if __name__ == "__main__":
	# read file into spreadsheet as list of lists of string
	unparsedList = []
	with open('Day08Input.txt', 'r') as myfile:
		for prog in myfile:
			unparsedList.append(prog.strip().split())
	# parse list and get list of all registers used
	parsedList = parseInsts(unparsedList)
	regVals = getAllRegisters(parsedList)
	# run instructions to update regVals
	runInsts(parsedList, regVals)
	print("Maximum value after execution: " + str(regVals[max(regVals, key=regVals.get)]) + " in register \"" + str(max(regVals, key=regVals.get)) + "\"")
	print("Largest value during execution: " + str(largestValue))