class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for word in strs:
            ans.append('*') 
            ans.append(str(len(word))) 
            ans.append('*') 
            ans.append(word)
        print(ans)
        return str("".join(ans))

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            if s[i] == '*':
                length = []
                i += 1
                while s[i]!='*':
                    length.append(s[i])
                    i+=1
                length = int(''.join(length))
                i += 1
                word = s[i:i+length]
                result.append(word)
                i += length
            else:
                i += 1
        return result