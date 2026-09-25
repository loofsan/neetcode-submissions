class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        charCounts1 = [0] * 26
        for i in range(len(s1)):
            charCounts1[ord(s1[i]) - ord("a")]+=1
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            newFreq = [0] * 26
            for i in range(len(s1)):
                newFreq[ord(s2[l+i]) - ord("a")]+=1
            if newFreq == charCounts1:
                return True
            r+=1
            l+=1
        
        return False