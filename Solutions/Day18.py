# solution to http://adventofcode.com/2017/day/18

class DuetProgram:

	def __init__(self, progNo, instList):
		self.instList = instList
		# initialize registers
		self.registers = {}
		for i in range(0, 26):
			letter = chr(97+i)
			if letter == "p":
				self.registers[letter] = progNo
			else:
				self.registers[chr(97+i)] = 0

	def getOperand(self, inst):
		# try to get literal first
		# if unsuccessful, use value of other register
		try:
			return int(inst[2])
		except ValueError:
			return self.registers[inst[2]]
		

	def runInsts(self):
		instList = self.instList
		lastPlayed = 0
		i = 0
		while (i < len(instList)):
			inst = instList[i]
			i += 1
			# print("Executing instruction: " + str(inst))
			if inst[0] == "snd":
				lastPlayed = self.registers[inst[1]]
			elif inst[0] == "set":
				operand = self.getOperand(inst)
				self.registers[inst[1]] = operand
			elif inst[0] == "add":
				operand = self.getOperand(inst)
				self.registers[inst[1]] += operand
			elif inst[0] == "mul":
				operand = self.getOperand(inst)
				self.registers[inst[1]] = self.registers[inst[1]] * operand
			elif inst[0] == "mod":
				operand = self.getOperand(inst)
				self.registers[inst[1]] = self.registers[inst[1]] % operand
			elif inst[0] == "rcv":
				if self.registers[inst[1]] == 0:
					continue
				else:
					print("Received sound: " + str(lastPlayed))
					break
			elif inst[0] == "jgz":
				if self.registers[inst[1]] == 0:
					continue
				else:
					operand = self.getOperand(inst)
					i += (operand - 1)
			# print("Registers: " + str(registers))
			# input("Next instruction...")

if __name__ == "__main__":
	instList = []
	with open("Day18Input.txt") as myfile:
		for line in myfile:
			instList.append(line.strip().split())
	
	prog0 = DuetProgram(0, instList)
	prog0.runInsts()