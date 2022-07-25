Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

Success
Details 
Runtime: 324 ms, faster than 12.89% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 74.16% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        
        res = [0] * (len(num1) + len(num2))
        num1,num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1+i2] += digit
                res[i1+i2+1] += (res[i1+i2]//10)
                res[i1+i2] = res[i2+i1] % 10
        
        
        res,start = res[::-1], 0
        
        while start <len(res) and res[start] == 0:
            start+=1
        
        
        res = map(str,res[start:])
        return "".join(res)