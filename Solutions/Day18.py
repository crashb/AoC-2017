# solution to http://adventofcode.com/2017/day/18

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

def getOperand(inst, registers):
	# try to get literal first
	# if unsuccessful, use value of other register
	try:
		return int(inst[2])
	except ValueError:
		return registers[inst[2]]
	

def runInsts(instList, registers):
	lastPlayed = 0
	i = 0
	while (i < len(instList)):
		inst = instList[i]
		i += 1
		# print("Executing instruction: " + str(inst))
		if inst[0] == "snd":
			lastPlayed = registers[inst[1]]
		elif inst[0] == "set":
			operand = getOperand(inst, registers)
			registers[inst[1]] = operand
		elif inst[0] == "add":
			operand = getOperand(inst, registers)
			registers[inst[1]] += operand
		elif inst[0] == "mul":
			operand = getOperand(inst, registers)
			registers[inst[1]] = registers[inst[1]] * operand
		elif inst[0] == "mod":
			operand = getOperand(inst, registers)
			registers[inst[1]] = registers[inst[1]] % operand
		elif inst[0] == "rcv":
			if registers[inst[1]] == 0:
				continue
			else:
				print("Received sound: " + str(lastPlayed))
				break
		elif inst[0] == "jgz":
			if registers[inst[1]] == 0:
				continue
			else:
				operand = getOperand(inst, registers)
				i += (operand - 1)
		# print("Registers: " + str(registers))
		# input("Next instruction...")

if __name__ == "__main__":
	instList = []
	with open("Day18Input.txt") as myfile:
		for line in myfile:
			instList.append(line.strip().split())
	
	registers0 = createRegs(0)
	runInsts(instList, registers0)