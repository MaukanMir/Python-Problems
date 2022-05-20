
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Success
Details 
Runtime: 101 ms, faster than 92.57% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 19.5 MB, less than 17.64% of Python3 online submissions for Top K Frequent Elements.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count, freq, res = {}, [[] for i in range(len(nums)+1)], []
        
        for num in nums:
            count[num] = count.get(num,0) +1
        
        for key,value in count.items():
            freq[value].append(key)
        
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
