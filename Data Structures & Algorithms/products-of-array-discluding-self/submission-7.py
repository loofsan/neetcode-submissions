class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        # Prefix run
        prefix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            res[i+1] *= prefix

        # Suffix run
        suffix = 1
        for i in range(len(nums) - 1, 0, -1):
            suffix *= nums[i]
            res[i-1] *= suffix
        
        return res
