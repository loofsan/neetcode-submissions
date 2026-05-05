class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res=[]
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = s[i:j]
            print(length)
            i = j + int(length)
            res.append(s[j+1:i+1])
            i+=1
        return res