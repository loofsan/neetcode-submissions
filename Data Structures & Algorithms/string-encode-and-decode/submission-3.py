class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for word in strs:
            ans.append(str(len(word)))
            ans.append('*')
            ans.append(word)
        
        return ''.join(ans)

    def decode(self, s: str) -> List[str]:
        
        i = 0
        words = []
        while i < len(s):
            length = []
            j = i 
            while s[j] != '*':
                length.append(s[j])
                j+=1    
     
            i = j + int(''.join(length))
            words.append(s[j+1:i+1])
            i+=1
        
        return words