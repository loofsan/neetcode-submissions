class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_pairs = {}
        for i, num in enumerate(nums):
            if target - num in num_pairs:
                return [num_pairs[target - num], i]
            
            num_pairs[num] = i
        
        return []