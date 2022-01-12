Check an array of values to determine if you can visit each value in a single cycle

def hasSingleCycle(array):
    
	visited =0
	currentIdx =0
	
	while visited < len(array):
		if visited >0 and currentIdx ==0:
			return False
		visited +=1
		currentIdx = getNext(currentIdx,array)
	
	return currentIdx ==0

def getNext(currentIdx,array):
	jump = array[currentIdx]
	nextIdx = (currentIdx + jump) % len(array)
	
	return nextIdx if nextIdx >=0 else nextIdx + len(array)
