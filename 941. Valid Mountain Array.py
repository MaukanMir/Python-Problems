
# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

# Success
# Details 
# Runtime: 214 ms, faster than 30.64% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.4 MB, less than 97.93% of Python3 online submissions for Valid Mountain Array.


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        length = len(arr)
        i =0
        
        while i+1 < length and arr[i] < arr[i+1]:
            i+=1
        
        if i ==0 or i == length-1:
            return False
        
        while i +1 < length and arr[i] > arr[i+1]:
            i+=1
        
        return i == length -1
