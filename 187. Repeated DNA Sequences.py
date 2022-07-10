The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Success
Details 
Runtime: 71 ms, faster than 89.47% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 26.1 MB, less than 71.43% of Python3 online submissions for Repeated DNA Sequences.


Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res,seen = set(), set()
        
        for l in range(len(s) -9):
            cur = s[l:l+10]

            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)
