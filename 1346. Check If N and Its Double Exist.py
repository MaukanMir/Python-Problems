
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# Example 2:

# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# Example 3:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.
 

# Success
# Details 
# Runtime: 116 ms, faster than 5.12% of Python3 online submissions for Check If N and Its Double Exist.
# Memory Usage: 14.1 MB, less than 98.96% of Python3 online submissions for Check If N and Its Double Exist.


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            first = arr[i]
            firstDoubled = first *2
            
            j =i+1
            
            while j< len(arr):
                second = arr[j]
                secondDoubled = second *2
                
                if first == secondDoubled or second == firstDoubled: return True
                
                j+=1
        
        return False

