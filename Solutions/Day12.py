# solution to http://adventofcode.com/2017/day/12

# gets the list of all vertices that are connected to a source vertex.
# graph[0] is a vertex, graph[0][0] and graph[0][1] are the paths
# returns list of visited vertices (list of int)
def getConnected(graph, source, visited = []):
	visited.append(source)
	currentNode = graph[source]
	for dest in currentNode:
		if dest not in visited:
			# print("Adding to visited: " + str(dest))
			getConnected(graph, dest, visited)
	return visited

# gets the number of distinct groups in a graph
# returns number of groups (int)
def getNumGroups(graph):
	visited = []
	numGroups = 0
	for i in range(0, len(graph)):
		if i not in visited:
			visited += getConnected(graph, i)
			numGroups += 1
	return numGroups
	

if __name__ == "__main__":
	# read input file into graph format:
	# graph[0] = [12, 67]
	# graph[1] = [89]
	# ...
	# means that node 0 has paths leading to 12 and 67, 1 has a path leading to 89, etc.
	connectionList = []
	with open('Day12Input.txt', 'r') as myfile:
		for line in myfile:
			unparsedLine = line.strip().split()
			parsedLine = []
			for i in range(2, len(unparsedLine)):
				connection = int(unparsedLine[i].replace(",", ""))
				parsedLine.append(connection)
			connectionList.append(parsedLine)
		
	connectedList = getConnected(connectionList, 0)
	print("Connected vertices: " + str(len(connectedList)))
	numGroups = getNumGroups(connectionList)
	print("Number of groups: " + str(numGroups))