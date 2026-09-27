class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charFreq = {}
        maxFreq = 0
        l, res = 0, 0

        for r in range(len(s)):
            
            charFreq[s[r]] = charFreq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, charFreq[s[r]])

            while ((r-l+1) - maxFreq) > k:
                charFreq[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)

        return res

                