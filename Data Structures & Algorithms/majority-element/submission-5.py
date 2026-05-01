class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1
        val = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                val = nums[i]
                count = 1
            elif val != nums[i]:
                count -= 1
            else:
                count += 1

        return val