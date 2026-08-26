class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # First pass to change the numbers
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        
        # Second pass to mark the numbers
        for num in nums:
            num = abs(num)
            if num > len(nums):
                continue
            if nums[num-1] > 0:
                nums[num-1]*=-1
        
        # Third pass to get the numbers
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1
        
        return len(nums) + 1 
        

