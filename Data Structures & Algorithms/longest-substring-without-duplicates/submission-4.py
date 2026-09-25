class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charSet = set()
        longest = 0
        while r < len(s):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l+=1
            charSet.add(s[r])
            r+=1
            longest = max(longest, len(charSet))
        
        return longest


