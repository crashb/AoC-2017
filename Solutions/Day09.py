# solution to http://adventofcode.com/2017/day/9

# cancel out any character denoted by "!"
def runCancels(inputString):
	output = ""
	cancel = False
	for char in inputString:
		if cancel:
			cancel = False
			continue
		if char == "!":
			cancel = True
			continue
		output += char
	return output

# remove garbage (denoted by "<>") from a string
# also prints the total amount of garbage characters removed
def cleanGarbage(inputString):
	output = ""
	garbage = False
	garbageRemoved = 0
	for char in inputString:
		if char == ">":
			# print("\">\" detected - setting garbage to false")
			garbage = False
			continue
		if garbage:
			garbageRemoved += 1
			continue
		if char == "<":
			# print("\"<\" detected - setting garbage to true")
			garbage = True
			continue
		output += char
	print("Total garbage removed: " + str(garbageRemoved))
	return output

# get a string's total score
def getScore(inputString):
	currentLevel = 0
	totalScore = 0
	for char in inputString:
		if char == "{":
			currentLevel += 1
			continue
		elif char == "}":
			totalScore += currentLevel
			currentLevel -= 1
			continue
	return totalScore

if __name__ == "__main__":
	inputString = ""
	with open('Day09Input.txt', 'r') as myfile:
		inputString = myfile.read()
	newString = runCancels(inputString)
	# print("Result after cancelling: " + newString)
	newString = cleanGarbage(newString)
	# print("Result after cleaning: " + newString)
	score = getScore(newString)
	print("Total score: " + str(score))