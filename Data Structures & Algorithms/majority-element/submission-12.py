class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, val = 0, 0
        for num in nums:
            if count == 0:
                val = num
                count += 1
            elif num != val:
                count -= 1
            else:
                count += 1
        
        return val