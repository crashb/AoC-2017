# solution to http://adventofcode.com/2017/day/1

# takes string as argument and returns the solution to the first captcha
# returns int solution
def solveCaptcha1(input):
	runningTotal = 0
	for i in range(0, len(input)):
		nextPlace = (i+1) % len(input)
		if input[i] == input[nextPlace]:
			runningTotal += int(input[i])
	return runningTotal

# takes string as argument and returns the solution to the second captcha
# returns int solution
def solveCaptcha2(input):
	runningTotal = 0
	for i in range(0, len(input)):
		nextPlace = int(i+len(input)/2) % len(input)
		if input[i] == input[nextPlace]:
			runningTotal += int(input[i])
	return runningTotal
		
if __name__ == "__main__":
	# read file into string
	with open('Day1Input.txt', 'r') as myfile:
		input = ''.join(myfile.read().strip().split('\n'))
		
	captchaSolution1 = solveCaptcha1(input)
	print("First captcha solution: " + str(captchaSolution1))
	captchaSolution2 = solveCaptcha2(input)
	print("Second captcha solution: " + str(captchaSolution2))
	