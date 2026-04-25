class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in hashmap:
                return [hashmap[other_num], i]
            hashmap[nums[i]] = i

        return [] 