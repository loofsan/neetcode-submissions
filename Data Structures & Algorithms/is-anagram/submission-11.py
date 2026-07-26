"""
- True if two strings are anagrams of each other
- False if not
- Question = "What kind of characters?"
    - lowercase?
    - uppercase?
    - symbols?
    - Numbers?
- If the two strings are empty, what do we return?
    - Are they anagrams or not

- Because we know that the strings only include lowercase letters,
    - it's limited to 26 characters

- We check if len of t == len of s
    - if two strings have different lengths,
    they cannot be anagrams of each other 
- They have the same len
    - We can create a charCount array
    - We can loop through one string
    - for characters we see in s, we add 1
    - for characters we see in c, we subtract 1
- we loop through charCount, if it's not 0, 
    - return False
- return True

- "racecar", "carrace"
- charCount = [1, 0, 2, ...]
- As we loop through, it will also be subtracting at the same time
- charCount = [0, 0, 0, ...]
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        charCount = [0] * 26
        for i in range(len(s)):
            charCount[ord(s[i]) - ord('a')] += 1
            charCount[ord(t[i]) - ord('a')] -= 1
        
        for num in charCount:
            if num != 0:
                return False
        
        return True
        