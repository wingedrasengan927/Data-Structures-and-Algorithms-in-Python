'''
Problem: https://leetcode.com/contest/weekly-contest-216/problems/smallest-string-with-a-given-numeric-value/
'''

class Solution:
    def getSmallestString(self, n, k):
        alphabets_value = list(range(1, 27))
        pointer = len(alphabets_value) - 1
        
        chars_used = 0
        result = []
        
        while chars_used < n:
            chars_used += 1
            if (k-alphabets_value[pointer]) < (n-chars_used):
                chars_used -= 1
                pointer -= 1
                continue
            result.append(pointer+1)
            k -= alphabets_value[pointer]
            
        result = list(reversed([chr(x+96) for x in result]))
        
        return "".join(result)