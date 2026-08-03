class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair of indices and temp        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                resT, resIndex = stack.pop()
                res[resIndex] = i - resIndex
            stack.append([t, i])

        return res