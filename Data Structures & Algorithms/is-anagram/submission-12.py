class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        charSet = [0] * 26

        for i in range(len(s)):

            charSet[ord(s[i]) - ord('a')] += 1
            charSet[ord(t[i]) - ord('a')] -= 1
        
        for num in charSet:
            if num != 0:
                return False
                
        return True