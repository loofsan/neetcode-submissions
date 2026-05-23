class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs)):
            res.append(str(len(strs[i])))
            res.append('#')
            res.append(strs[i])

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + length
            res.append(s[j+1:i+1])
            i+=1
        return res
