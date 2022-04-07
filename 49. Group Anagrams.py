Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


Success
Details 
Runtime: 107 ms, faster than 85.50% of Python3 online submissions for Group Anagrams.
Memory Usage: 18.4 MB, less than 35.47% of Python3 online submissions for Group Anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        
        for word in strs:
            ans[tuple(sorted(word))].append(word)
        return ans.values()
Success
Details 
Runtime: 120 ms, faster than 73.55% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.9 MB, less than 17.19% of Python3 online submissions for Group Anagrams.

 
 class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')]+=1
            ans[tuple(count)].append(word)
        return ans.values()
