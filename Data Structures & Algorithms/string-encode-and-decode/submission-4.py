class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
            
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        
        i, res = 0, []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + length
            res.append(s[j+1:i+1])
            i+=1
        
        return res

