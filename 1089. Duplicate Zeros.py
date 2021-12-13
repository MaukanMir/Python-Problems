# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Success
Details 
Runtime: 64 ms, faster than 94.47% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.8 MB, less than 84.26% of Python3 online submissions for Duplicate Zeros.


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        total = arr.count(0)
        size = len(arr)
        
        for i in range(size-1,-1,-1):
            if i + total < size: arr[i+total] =arr[i]
            
            if arr[i] == 0:
                total -=1
                if i +total < size: arr[i+total] =0
        return
        
