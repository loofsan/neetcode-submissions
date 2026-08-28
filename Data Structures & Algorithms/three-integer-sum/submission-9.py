"""
[-4, -1, -1, 0, 1, 2]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        seen = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1

            while j < k:
                if j == i:
                    j+=1
                elif k == i:
                    k-=1
                
                if nums[i] + nums[j] + nums[k] < 0:
                    j +=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        seen.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
            
        return list(seen)
