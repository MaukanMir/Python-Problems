You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1.

Return the sum of each integer in nestedList multiplied by its weight.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1.
1*3 + 4*2 + 6*1 = 17
 

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.


Success
Details 
Runtime: 33 ms, faster than 53.17% of Python3 online submissions for Nested List Weight Sum II.
Memory Usage: 14.6 MB, less than 24.47% of Python3 online submissions for Nested List Weight Sum II.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        depthAccumulator = []
        
        for nestedInt in nestedList:
            ProcessNestedInteger(nestedInt, 0, depthAccumulator)
        
        total =0
        
        for idx, val in enumerate(depthAccumulator):
            multi = len(depthAccumulator) -idx
            total += multi * val
        return total
def ProcessNestedInteger(nestedInteger,curr,depthAccumulator):
        if curr >= len(depthAccumulator):
            depthAccumulator.append(0)
        if nestedInteger.isInteger():
            depthAccumulator[curr] += nestedInteger.getInteger()
            return
        
        for l in nestedInteger.getList():
            ProcessNestedInteger(l,curr+1, depthAccumulator)
