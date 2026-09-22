class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r and l != r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                elif threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
        
        return list(res)

