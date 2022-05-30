Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Success
Details 
Runtime: 44 ms, faster than 62.08% of Python3 online submissions for Permutations.
Memory Usage: 14.1 MB, less than 94.36% of Python3 online submissions for Permutations.


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        values = []
        def backtrack(first =0):
            if first ==n:
                values.append(nums[:])
                
            for i in range(first,n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        backtrack()
        return values

       
       
Success
Details 
Runtime: 42 ms, faster than 85.83% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 58.46% of Python3 online submissions for Permutations.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        if len(nums) ==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
            
        return res
