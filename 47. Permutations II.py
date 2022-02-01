Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

Success
Details 
Runtime: 60 ms, faster than 80.71% of Python3 online submissions for Permutations II.
Memory Usage: 14.4 MB, less than 88.85% of Python3 online submissions for Permutations II.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
      
        result, perm, count  = [],[], { k:nums.count(k) for k in nums}
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for n in count:
                if count[n] >0:
                    perm.append(n)
                    count[n] -=1
                    
                    backtrack()
                    count[n] +=1
                    perm.pop()
        backtrack()          
        return result
