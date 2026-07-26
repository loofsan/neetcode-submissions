class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        currNum = 0

        for num in nums:
            if count == 0:
                currNum = num
                count+=1
            elif currNum == num:
                count += 1
            else:
                count -= 1
        
        return currNum
        