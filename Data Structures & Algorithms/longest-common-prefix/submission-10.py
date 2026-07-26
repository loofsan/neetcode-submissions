"""
Question
    - What if strs is empty?
        - return ""

- We create an array called res to return 
- We are going to do a columnar loop
    - We loop through the letters in first word using index
        - We loop through the words in strs
            - if the letter doesn't match with the letter in firstWord or
            if the index is > than the len of the word
                - return ''.join(res)
    
- return ''.join(res)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        firstWord = strs[0]
        if len(strs) == 1:
            return firstWord
    
        res = []
        for i in range(len(firstWord)):
            for word in strs:
                if i >= len(word) or word[i] != firstWord[i]:
                    return ''.join(res)
            
            res.append(firstWord[i])
        
        return ''.join(res)

"""
strs = ["bat","bag","bank","band"]
firstWord = "bat"
res = ["b", "a", ]

"""
