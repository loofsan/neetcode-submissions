"""
- every input has exactly one pair
- return indices (with the smaller index first)

- We use a hashmap.
    - the hashmap will contain the curr num as the key and index as value

- We will loop through every num in nums
- if target - num in the hashmap:
    - we return [hashmap[target - num], i]
- we add the current num to hashmap with its index
- return [] (But we know there will always be a pair 
so we don't really need this either)
     
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checkAdj = {}
        for i, num in enumerate(nums):
            adj = target - num
            if adj in checkAdj:
                return [checkAdj[adj], i]
            checkAdj[num] = i
        
        return []