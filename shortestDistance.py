# 243. Shortest Word Distance
# Easy

# 859

# 72

# Add to List

# Share
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
 

# Constraints:

# 1 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2


Success
Details 
Runtime: 64 ms, faster than 85.19% of Python3 online submissions for Shortest Word Distance.
Memory Usage: 18 MB, less than 15.72% of Python3 online submissions for Shortest Word Distance.
  
  
  
  
  
  class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        indexOne,indexTwo = -1,-1
        min_distance = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1: indexOne = i
            elif wordsDict[i] == word2:indexTwo = i
            
            
            if indexOne != -1 and indexTwo != -1:
                
                min_distance = min(min_distance, abs(indexOne- indexTwo))
        return min_distance
