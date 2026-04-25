class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for i in strs:
            if ''.join(sorted(i)) in anaDict:
                anaDict[''.join(sorted(i))].append(i)

            else:
                anaDict[''.join(sorted(i))] = [i]

        finalList = []

        for i in anaDict.keys():
            finalList.append(anaDict[i])

        return finalList