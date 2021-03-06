# solution to http://adventofcode.com/2017/day/15

# given an int value that was generated by generator A, get the next value
# returns next value (int)
def nextValueA1(prevValue):
	nextValue = prevValue * 16807
	return nextValue % 2147483647

# given an int value that was generated by generator B, get the next value
# returns next value (int)
def nextValueB1(prevValue):
	nextValue = prevValue * 48271
	return nextValue % 2147483647
	
# given an int value that was generated by generator A, get the next value
# only returns values that are multiples of 4, as per part 2
# returns next value (int)
def nextValueA2(prevValue):
	nextValue = prevValue
	while(True):
		nextValue = nextValue * 16807
		nextValue = nextValue % 2147483647
		if nextValue % 4 == 0:
			return nextValue

# given an int value that was generated by generator B, get the next value
# only returns values that are multiples of 8, as per part 2
# returns next value (int)
def nextValueB2(prevValue):
	nextValue = prevValue
	while(True):
		nextValue = nextValue * 48271
		nextValue = nextValue % 2147483647
		if nextValue % 8 == 0:
			return nextValue
	
# checks if the last 16 bits of two numbers match.
# returns boolean
def checkMatch(valueA, valueB):
	bitMask = 0xFFFF
	maskedA = valueA & bitMask
	maskedB = valueB & bitMask
	return (maskedA == maskedB)
	
# checks 40 000 000 values from generators A1 and B1 for a match
# returns number of matches (int)
def countMatches1(valueA, valueB):
	print("Finding matches for part 1...")
	matches = 0
	for i in range(0, 40000000):
		# show progress while working
		if i % 10000000 == 0:
			print("After " + str(i) + " pairs, " + str(matches) + " matches found")
		if checkMatch(valueA, valueB):
			matches += 1
		valueA = nextValueA1(valueA)
		valueB = nextValueB1(valueB)
	return matches
	
# checks 40 000 000 values from generators A2 and B2 for a match
# returns number of matches (int)
def countMatches2(valueA, valueB):
	print("Finding matches for part 2...")
	matches = 0
	for i in range(0, 5000000):
		# show progress while working
		if i % 1000000 == 0:
			print("After " + str(i) + " pairs, " + str(matches) + " matches found")
		if checkMatch(valueA, valueB):
			matches += 1
		valueA = nextValueA2(valueA)
		valueB = nextValueB2(valueB)
	return matches

if __name__ == "__main__":
	initialA = 634
	initialB = 301
	result1 = countMatches1(initialA, initialB)
	print("Result for Part 1: " + str(result1))
	result2 = countMatches2(initialA, initialB)
	print("Result for Part 2: " + str(result2))