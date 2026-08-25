class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        biggest = 0
        for num in nums:
            res = []
            if num-1 in numSet:
                continue
            while num in numSet:
                res.append(num)
                num+=1
            biggest = max(len(res), biggest)
                
        
        return biggest