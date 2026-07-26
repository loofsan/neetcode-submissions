"""
- Can there ever be an empty strs?
- For each string in strs, what can the characters be?
    - lowercase, uppercase, special char, num

- groups = defaultdict(list)
- for word in strs:
    - we create a charCount array 
    - we turn that into a tuple and add the word as value
- return groups.values()
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for word in strs:
            charCount = [0] * 26
            for c in word:
                charCount[ord(c) - ord('a')] += 1
            groups[tuple(charCount)].append(word)
        
        return list(groups.values())

# strs = ["act","pots","tops","cat","stop","hat"]
# groups = {(1, 0, 1...): ["act"], }
