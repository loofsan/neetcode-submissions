class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = []

        for n in range(len(nums)):
            if nums[n] in set:
                return True
            set.append(nums[n])
        return False
         