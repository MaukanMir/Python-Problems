Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
 

Constraints:

2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000

Success
Details 
Runtime: 376 ms, faster than 20.55% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.3 MB, less than 62.99% of Python3 online submissions for Sort Array By Parity II.


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        leftPointer, rightPointer = 0,len(nums)-1
        
        while leftPointer < rightPointer:
            if nums[leftPointer] %2 ==0 and leftPointer %2 ==0 or nums[leftPointer] %2 !=0 and leftPointer %2 !=0:
                leftPointer +=1

            if nums[leftPointer] %2 !=0 and leftPointer %2 ==0 :
                leftPointer,nums =  evenPositions(leftPointer,nums)

            if nums[leftPointer] %2 ==0 and leftPointer %2 !=0:
                leftPointer, nums =  oddPositions(leftPointer,nums)
        return nums

def evenPositions(leftPointer, nums):
  
    for i in range(leftPointer+1, len(nums)):
        if  nums[i] %2 ==0:
            nums[leftPointer], nums[i] = nums[i], nums[leftPointer]
            break
    return leftPointer+1, nums
def oddPositions(leftPointer, nums):
  
    for i in range(leftPointer+1, len(nums)):
        if  nums[i] %2 !=0:
            nums[leftPointer], nums[i] = nums[i], nums[leftPointer]
            break
    return leftPointer+1, nums
