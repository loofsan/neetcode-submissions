"""
- We create a set of numbers
- We loop through nums
    - if num is in the set:
        - we return False
    we append num to set
- return True

- [1, 2, 1, 3, 4]
- set = (1, 2)
- num = 1
- False
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        checkDup = set()
        for num in nums:
            if num in checkDup:
                return True
            checkDup.add(num)
        
        return False