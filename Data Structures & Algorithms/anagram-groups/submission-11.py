class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            charSet = [0] * 26
            for c in word:
                charSet[ord(c) - ord("a")] += 1
            
            anagrams[tuple(charSet)].append(word)
        
        return list(anagrams.values())