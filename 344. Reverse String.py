# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


Success
Details 
Runtime: 202 ms, faster than 50.76% of Python3 online submissions for Reverse String.
Memory Usage: 18.6 MB, less than 62.27% of Python3 online submissions for Reverse String.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left =0 
        right = len(s)-1
        while left < right:
            helper(s,left,right)
            
            left +=1
            right -=1
    
def helper(array, left,right):
        array[left],array[right] = array[right],array[left]
        
        return left,right,array
