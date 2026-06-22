class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord('a')] += 1
            hashMap[tuple(char_count)].append(word)
        
        return list(hashMap.values())