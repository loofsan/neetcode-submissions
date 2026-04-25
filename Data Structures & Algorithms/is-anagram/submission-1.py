class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1 = 0
        count2 = 0

        hashMap1 = {}
        hashMap2 = {}

        for i in range(len(s)):
            count1 += ord(s[i])
            if s[i] in hashMap1:
                hashMap1[s[i]]+=1
            else:
                hashMap1[s[i]] = 1
            count2 += ord(t[i])
            if t[i] in hashMap2:
                hashMap2[t[i]]+=1
            else:
                hashMap2[t[i]] = 1
        
        if count1 == count2 and hashMap1 == hashMap2:
            return True
        
        return False