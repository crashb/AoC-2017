# solution to http://adventofcode.com/2017/day/4

# getLinesFromFile takes a filepath as an argument, and returns the list of lines in the file

# checks a list of passphrases (list of lists of words)
# returns the number of passphrases which do not have any duplicate words (int)
# rank: 400
def countValid1(phraseList):
	numValid = 0
	for phrase in phraseList:
		if len(phrase) == len(set(phrase)):
			numValid += 1
	return numValid

# checks a list of passphrases (list of lists of words)
# returns the number of passphrases which do not have any words that are anagrams of each other (int)
# rank: 307
def countValid2(phraseList):
	numValid = 0
	for phrase in phraseList:
		# sort letters alphabetically in each word
		for i in range(0, len(phrase)):
			phrase[i] = ''.join(sorted(phrase[i]))
		if len(phrase) == len(set(phrase)):
			numValid += 1
	return numValid
	
if __name__ == "__main__":
	lineList = []
	with open('Day4Input.txt', 'r') as myfile:
		for row in myfile:
			lineList.append(row.split())
	answer1 = countValid1(lineList)
	print("Answer to part 1: " + str(answer1))
	answer2 = countValid2(lineList)
	print("Answer to part 2: " + str(answer2))