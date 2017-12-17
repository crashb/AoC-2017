# solution to http://adventofcode.com/2017/day/17

# fills a buffer of length steps+1 with numbers according to part 1
# returns the buffer (list of int)
def fillBuffer(stepLength, steps):
	buffer = [0]
	currentPos = 0
	for i in range(1, steps + 1):
		currentPos = (currentPos + stepLength) % len(buffer)
		currentPos += 1
		buffer.insert(currentPos, i)
	return buffer
	
# finds the number after zero in a buffer of length steps+1
# returns the number after zero (int)
def findAfterZero(stepLength, steps):
	currentPos = 0
	lastChanged = 1
	for i in range(1, steps + 1):
		currentPos = ((currentPos + stepLength) % i) + 1
		if currentPos == 1:
			lastChanged = i
	return lastChanged
	
if __name__ == "__main__":
	stepLength = 303
	buffer = fillBuffer(stepLength, 2017)
	print("2017 location: " + str(buffer.index(2017)))
	print("Number in buffer after 2017: " + str(buffer[buffer.index(2017) + 1]))
	
	afterZero = findAfterZero(stepLength, 50000000)
	print("Number after 0 after 50000000 steps: " + str(afterZero))