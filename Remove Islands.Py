# Graph Problem:
#   Remove all the interior ones in a 2D array where none of the ones are connected to the edges of the graph. 
  
  
  
  def removeIslands(matrix):
    onesBorder = [[False for value in matrix[0]] for row in matrix]
	
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			rowIsBorder = row ==0 or row == len(matrix)-1
			colIsBorder = col == 0 or col == len(matrix[row])-1
			isBorder = rowIsBorder or colIsBorder
			
			if not isBorder:
				continue
			
			if matrix[row][col] !=1:
				continue
			
			
			findOnes(matrix,row,col,onesBorder)
			
	for row in range(1,len(matrix)):
		for col in range(1,len(matrix[0])):
			if onesBorder[row][col]:
				continue
			
			matrix[row][col] = 0
	return matrix

def findOnes(matrix,startRow,startCol,onesBorder):
	stack = [(startRow,startCol)]
	
	while len(stack) >0:
		currentPosition = stack.pop()
		currentRow,currentCol = currentPosition
		
		alreadyVisited = onesBorder[currentRow][currentCol]
		if alreadyVisited:
			continue
		
		onesBorder[currentRow][currentCol] = True
		neighbors = getNeighbors(matrix,currentRow,currentCol)
		for neighbor in neighbors:
			row,col = neighbor
			if matrix[row][col] !=1:
				continue
			
			stack.append(neighbor)

def getNeighbors(matrix,row,col):
	neighbors = []
    numRows = len(matrix)
	numCols = len(matrix[row])
	
	if row -1 >=0: 
		neighbors.append((row-1, col))
	if row +1 <numRows:
		neighbors.append((row+1,col))
	if col-1 >=0:
		neighbors.append((row,col-1))
	if col +1 < numCols:
		neighbors.append((row,col+1))
	
	return neighbors
