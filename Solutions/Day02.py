# solution to http://adventofcode.com/2017/day/2

# calculates first checksum from 2d list of int representing spreadsheet
# returns int checksum
def getChecksum1(spreadsheet):
	checksum = 0
	for row in spreadsheet:
		checksum += max(row) - min(row)
	return checksum

# calculates second checksum from 2d list of int representing spreadsheet
# returns int checksum
def getChecksum2(spreadsheet):
	checksum = 0
	for row in spreadsheet:
		for i in range(0, len(row)):
			for j in range(0, len(row)):
				if (row[i] % row[j] == 0) and (i != j):
					checksum += row[i] / row[j]
	return int(checksum)

if __name__ == "__main__":
	# read file into spreadsheet (2d list of strings)
	spreadsheet = []
	with open('Day02Input.txt', 'r') as myfile:
		for row in myfile:
			spreadsheet.append(row.split())
			
	# convert strings in spreadsheet to int
	intSpreadsheet = []
	for row in spreadsheet:
		intSpreadsheet.append([int(numeric_string) for numeric_string in row])
			
	checksum1 = getChecksum1(intSpreadsheet)
	print("First checksum: " + str(checksum1))
	checksum2 = getChecksum2(intSpreadsheet)
	print("Second checksum: " + str(checksum2))
	