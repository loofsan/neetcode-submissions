class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # left to right
        prefixL = 1
        for i in range(1, len(nums)):
            prefixL *= nums[i - 1]
            res[i] = prefixL
        
        prefixR = 1
        for i in range(len(nums) - 1, 0, -1):
            prefixR *= nums[i]
            res[i - 1] *= prefixR
        
        return res