Get the longest river sizes in a 2d array where 1's represent the rivers and 0's represent the islands. Find the longest river size.

def riverSizes(matrix):
    sizes = []
	visited = [[False for value in row] for row in matrix]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:continue
			
			traverseNode(i,j,matrix,visited, sizes)
	return sizes

def traverseNode(i,j,matrix,visited,sizes):
	currentRiverSize =0
	nodesToExplore = [[i,j]]
	
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop()
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0: continue
		
		currentRiverSize +=1
		unvistedN = getUnVisited(i,j,matrix,visited)
		for neighbor in unvistedN:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0: sizes.append(currentRiverSize)

def getUnVisited(i,j, matrix,visited):
		unvistedN = []
		if i >0 and not visited[i-1][j]:
			unvistedN.append([i-1,j])
		if i < len(matrix)-1 and not visited[i+1][j]: 
			unvistedN.append([i+1,j])
		if j > 0 and not visited[i][j-1]:
			unvistedN.append([i,j-1])
		if j < len(matrix[0])-1 and not visited[i][j+1]:
			unvistedN.append([i,j+1])
	    return unvistedN
