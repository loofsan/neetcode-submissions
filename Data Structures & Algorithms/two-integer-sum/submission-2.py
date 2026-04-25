class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}

        for i, num in enumerate(nums):

            other_num = target - num
            if other_num in res:
                return [res[other_num], i]
            
            res[num] = i
        
        return []