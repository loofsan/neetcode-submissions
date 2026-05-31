class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        prefix = 0
        count = {0 : 1}

        for num in nums:
            prefix += num
            diff = prefix - k

            res += count.get(diff, 0)
            count[prefix] = count.get(prefix, 0) + 1
        
        return res

            

            
