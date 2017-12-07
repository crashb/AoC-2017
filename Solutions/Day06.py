# solution to http://adventofcode.com/2017/day/6

# takes list of initial memory bank state
# returns number of cycles taken to hit a loop (int)
def countCycles(memBanks):
	configs = []
	configs.append(list(memBanks))
	cycles = 1
	while (True):
		# redistribute block with most memory
		memToSpread = max(memBanks)
		spreadIndex = memBanks.index(memToSpread)
		memBanks[spreadIndex] = 0
		while (memToSpread > 0):
			spreadIndex = (spreadIndex + 1) % len(memBanks)
			memBanks[spreadIndex] += 1
			memToSpread -= 1
		# check if we have a config we've seen before
		if memBanks in configs:
			return cycles
		else:
			configs.append(list(memBanks))
			cycles += 1
			
if __name__ == "__main__":
	# read file into spreadsheet (2d list of strings)
	memBanks = []
	with open('Day06Input.txt', 'r') as myfile:
		memBanks = myfile.readline().split()
	for i in range(0, len(memBanks)):
		memBanks[i] = int(memBanks[i])
	print("Memory bank contents: " + str(memBanks))
	numCycles = countCycles(memBanks)
	print("Number of cycles before loop: " + str(numCycles))
	# because the function edits the list that is provided to it as an argument,
	# calling it again will return the length of the loop (neatly enough)
	loopLength = countCycles(memBanks)
	print("Number of cycles in a loop: " + str(loopLength))
	