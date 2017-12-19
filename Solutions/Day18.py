# attempt at http://adventofcode.com/2017/day/18
# does not work.

deadlocked = 0
programSent = 0

def createRegs(progNo):
	# initialize registers
	registers = {}
	for i in range(0, 26):
		letter = chr(97+i)
		if letter == "p":
			registers[letter] = progNo
		else:
			registers[chr(97+i)] = 0
	return registers

def getOperand(inst, registers, index=2):
	# try to get literal first
	# if unsuccessful, use value of other register
	try:
		return int(inst[index])
	except ValueError:
		return registers[inst[index]]
	

def runInsts(instList, startPos, registers, rcvList = [], program1=False):
	global deadlocked
	global programSent
	# print("Starting program at instruction " + str(startPos))
	i = startPos
	sndList = []
	while (i < len(instList)):
		inst = instList[i]
		i += 1
		# print("Executing instruction: " + str(inst))
		if inst[0] == "snd":
			operand = getOperand(inst, registers, 1)
			# print("Sending " + str(operand) + " to other program")
			if program1:
				programSent += 1		
			sndList.append(operand)
		elif inst[0] == "set":
			operand = getOperand(inst, registers)
			registers[inst[1]] = operand
		elif inst[0] == "add":
			operand = getOperand(inst, registers)
			registers[inst[1]] += operand
		elif inst[0] == "mul":
			operand = getOperand(inst, registers)
			registers[inst[1]] *= operand
		elif inst[0] == "mod":
			operand = getOperand(inst, registers)
			registers[inst[1]] %= operand
		elif inst[0] == "rcv":
			if rcvList != []:
				# print("Received " + str(rcvList[0]) + " from other program")
				registers[inst[1]] = rcvList[0]
				del rcvList[0]
			else:
				# print("RCVList is empty!")
				deadlocked += 1
				return [i-1, list(sndList)]
		elif inst[0] == "jgz":
			operand = getOperand(inst, registers, 1)
			if operand == 0:
				continue
			else:
				operand = getOperand(inst, registers)
				i += (operand - 1)
		# if we complete a full instruction, reset deadlocked counter
		deadlocked = 0
		# print("Registers: " + str(registers))
		# input("Next instruction: " + str(i))
	# deadlocked = 2
	return[-1, []]

if __name__ == "__main__":
	instList = []
	with open("Day18Input.txt") as myfile:
		for line in myfile:
			instList.append(line.strip().split())
	
	registers0 = createRegs(0)
	registers1 = createRegs(1)
	startPos1 = 0
	startPos2 = 0
	sendingList1 = []
	sendingList2 = []
	while deadlocked < 2:
		# print("Sending to program 0: " + str(sendingList2))
		result1 = runInsts(instList, startPos1, registers0, sendingList2)
		# print("Result of program 0: " + str(result1))
		# print("Deadlocked value: " + str(deadlocked))
		startPos1 = result1[0]
		sendingList1 = result1[1]
		# print("Sending to program 1: " + str(sendingList1))
		result2 = runInsts(instList, startPos2, registers1, sendingList1, True)
		# print("Result of program 1: " + str(result2))
		# print("Deadlocked value: " + str(deadlocked))
		startPos2 = result2[0]
		sendingList2 = result2[1]
	print("Number of times program 1 sent a value: " + str(programSent))