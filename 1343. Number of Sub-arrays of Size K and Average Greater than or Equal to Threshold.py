Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


Success
Details 
Runtime: 1043 ms, faster than 20.20% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.
Memory Usage: 26.7 MB, less than 97.43% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        total = sum(arr[:k])
        
        score = 1 if total//k >= threshold else 0
        
        
        for i in range(1,len(arr)-k+1):
            total -= arr[i-1]
            total += arr[i+k-1]
            
            if total// k >= threshold:score +=1
        return score
