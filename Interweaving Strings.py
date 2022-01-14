Write a function that takes in three strings and returns a boolean representing whether the third string can be formed by interweaving the first two strings.

def interweavingStrings(one, two, three):
	if len(three) != len(one) + len(two):
		return False
	
	cache = [[None for col in range(len(two)+1)] for i in range(len(one)+1)]
	return match(one,two,three,0,0,cache)
def match(one,two,three,i,j,cache):
	if cache[i][j] is not None:
		return cache[i][j]
	k = i +j
	if k== len(three):return True
	
	if i < len(one) and one[i] == three[k]:
		cache[i][j] = match(one,two,three, i+1,j,cache)
		if cache[i][j]:
			return True
	
	if j < len(two) and two[j] == three[k]:
		cache[i][j] = match(one,two,three,i,j+1, cache)
		return cache[i][j]
	cache[i][j] = False
	
	return False
 
