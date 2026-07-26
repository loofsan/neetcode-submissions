"""
- We first create a new array of length 2n, res
- Then, as we loop through nums,
    - we assign the num at res[i] and res[i + len(nums)]

- [1, 2, 3, 4]
- [0, 1, 2, 3]
- [1, 2, 3, 4, 1, 2, 3, 4]
- [0, 1, 2, 3, 4, 5, 6, 7]
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums) * 2
        for i in range(len(nums)):
            res[i] = res[i + len(nums)] = nums[i]
        
        return res