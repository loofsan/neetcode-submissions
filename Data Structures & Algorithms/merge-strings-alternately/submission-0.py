class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]

        if len(word1) == len(word2):
            for i in range(len(word1)):
                res.append(word1[i])
                res.append(word2[i])
        
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                res.append(word1[i])
                res.append(word2[i])
            for i in range(len(word1),len(word2)):
                res.append(word2[i])
        
        elif len(word2) < len(word1):
            for i in range(len(word2)):
                res.append(word1[i])
                res.append(word2[i])
            for i in range(len(word2),len(word1)):
                res.append(word1[i])
        
        return ''.join(res)