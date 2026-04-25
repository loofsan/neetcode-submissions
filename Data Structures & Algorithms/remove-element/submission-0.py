class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0
        
        left = 0
        right = len(nums) - 1

        if left == right:
            if nums[0] == val:
                return 0
            return 1

        while left < right:

            if nums[left] != val:
                left += 1

            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]

            else:
                right -= 1

        k = 0
        for num in nums:
            if num != val:
                k+=1
        
        return k