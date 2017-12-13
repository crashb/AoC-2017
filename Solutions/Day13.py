# solution to http://adventofcode.com/2017/day/13

# given a dictionary of the layers {layerID, layerDepth} and a number of cycles to wait,
# find the severity of the path
# returns severity (int)
# rank: 742
def getSeverity(layerList, waitCycles):
	severity = 0
	cycles = waitCycles
	for i in range(0, max(layerList) + 1):
		if i not in layerList:
			cycles += 1
			continue
		scannerPos = cycles % (2*layerList[i] - 2)
		if scannerPos == 0:
			severity += i * layerList[i]
		cycles += 1
	return severity
	

if __name__ == "__main__":
	layerList = {}
	with open('Day13Input.txt', 'r') as myfile:
		for line in myfile:
			unparsedLine = line.strip().split()
			layerNum = int(unparsedLine[0].replace(":", ""))
			layerList[layerNum] = int(unparsedLine[1])
	severity = getSeverity(layerList, 0)
	print("Severity on travelling instantly: " + str(severity))
	# keep trying values for delay until we get one that never hits a scanner
	# probably not the most efficient solution, but it works	
	# rank: 348
	i = 1
	while (True):
		trialSeverity = getSeverity(layerList, i)
		# specify that we want to avoid the first drone (even though severity of hitting it is 0)
		if trialSeverity == 0 and (i % (2*layerList[0] - 2) != 0):
			break
		i += 1
	print("Picoseconds to wait to avoid detection: " + str(i))