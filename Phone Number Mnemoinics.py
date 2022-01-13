# Phone Number Mnemoinics

# Map a numeric string to the possible combinations in a celluar phone. Return a list of all of these letter combinations.
# Solution 1:

def phoneNumberMnemonics(phoneNumber):
	
	digits ={
		"0": ["0"],
		"1":["1"],
		"2":["a","b","c"],
		"3":["d","e","f"],
		"4":["g","h","i"],
		"5":["j","k","l"],
		"6":["m","n","o"],
		"7":["p","q","r","s"],
		"8":["t","u","v"],
		"9":["w","x","y","z"],
	}
	seen = []
	combos = [digits[n] for n in phoneNumber]
	
	def backtrack(i,curStr):
		if len(curStr) == len(phoneNumber):
			seen.append(curStr)
			return
		
		for num in combos[i]:
			backtrack(i+1,curStr + num)
	
	backtrack(0,"")
	return seen


# Solution 2:
	
	def phoneNumberMnemonics(phoneNumber):
	currentNumber = ["0"] * len(phoneNumber)
	found = []
	
	phoneHelper(0,phoneNumber,currentNumber,found)
	return found

def phoneHelper(idx,phoneNumber,currentNumber,found):
	digits ={
		"0": ["0"],
		"1":["1"],
		"2":["a","b","c"],
		"3":["d","e","f"],
		"4":["g","h","i"],
		"5":["j","k","l"],
		"6":["m","n","o"],
		"7":["p","q","r","s"],
		"8":["t","u","v"],
		"9":["w","x","y","z"],
	}
	if idx == len(phoneNumber):
		got = "".join(currentNumber)
		found.append(got)
	else:
		digit = phoneNumber[idx]
		letters = digits[digit]
		
		for letter in letters:
			currentNumber[idx] = letter
			phoneHelper(idx+1, phoneNumber,currentNumber,found)
