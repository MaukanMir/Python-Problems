Create subsets of an array of integers using recurison

def powerset(array, idx =None):
    if idx == None:
		idx = len(array) -1
	if idx <0:
		return [[]]
	
	got = array[idx]
	subsets =powerset(array,idx-1)
	for i in range(len(subsets)):
		currentSubset = subsets[i]
		subsets.append(currentSubset + [got])
	return subsets
