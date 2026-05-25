class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hashSet:
                count = num
                length = 1
                while count + 1 in hashSet:
                    length += 1
                    count += 1

                longest = max(length, longest)
        
        return longest