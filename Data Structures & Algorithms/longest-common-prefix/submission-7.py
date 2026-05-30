class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        firstWord = strs[0]
        res = []
        for i in range(len(firstWord)):
            for word in strs:
                if i == len(word) or word[i] != firstWord[i]:
                    return ''.join(res)
            res.append(word[i])

        return ''.join(res)  
