Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].


Success
Details 
Runtime: 1175 ms, faster than 32.30% of Python3 online submissions for Minimum Swaps to Group All 1's Together.
Memory Usage: 17 MB, less than 99.47% of Python3 online submissions for Minimum Swaps to Group All 1's Together.


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ones, left , right , count , maxValue = sum(data), 0, 0,0, float('-inf')
        
        while right < len(data):
            count += data[right]
            right+=1
            
            if right - left > ones:
                count -= data[left]
                left +=1
            
            maxValue = max(maxValue, count)
        return ones - maxValue
        
