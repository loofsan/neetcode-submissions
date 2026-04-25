class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This is the first solution
        # if len(s) != len(t):
        #     return False
        # a = sorted(s)
        # b = sorted(t)

        # if a == b:
        #     return True
        # else:
        #     return False

        # This is the second solution
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
             return False

        for n in range(len(s)):

            if s[n] in dict1:
                dict1[s[n]] += 1
            else:
                dict1.update({s[n]: 1})

        for n in range(len(t)):

            if t[n] in dict2:
                dict2[t[n]] += 1
            else:
                dict2.update({t[n]: 1})

        if dict1 == dict2:
            return True
        else:
            return False
