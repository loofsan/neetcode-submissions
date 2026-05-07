class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for num in nums:
            if count == 0:
                count+=1
                val=num
            if val != num:
                count-=1
            else:
                count+=1
        
        return val