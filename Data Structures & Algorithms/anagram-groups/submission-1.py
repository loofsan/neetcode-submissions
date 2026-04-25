class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            fix = ''.join(sorted(strs[i]))
            if fix in hashMap:
                hashMap[fix].append(strs[i])
            else:
                hashMap[fix] = [strs[i]]

        result = []
        for key in hashMap.keys():
            result.append(hashMap[key])

        return result