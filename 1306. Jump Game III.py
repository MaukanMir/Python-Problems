Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.



Success
Details 
Runtime: 312 ms, faster than 93.25% of Python3 online submissions for Jump Game III.
Memory Usage: 20.6 MB, less than 96.06% of Python3 online submissions for Jump Game III.


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = [start]
        while q:
            
            val = q.pop()
            if arr[val] == -1:
                continue
            if arr[val] ==0:
                return True
            left,right = val - arr[val],  arr[val] + val
            
            if 0<= left < len(arr):
                q.append(left)
            if 0<= right < len(arr):
                q.append(right)
            arr[val] = -1
        return False
