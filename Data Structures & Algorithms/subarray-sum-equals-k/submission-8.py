"""
subarray = prefix - k

{
0: 1
}

Start with hashmap 0:1

prefix = 0
Go through the loop:
    - add up the prefix
    - is prefix - k in the hashmap?
        - if yes, we add +1 to the count of the subarray
    add prefix to the hashmap with the count 0

nums = [4,4,4,4,4,4], k = 4
pref = 12
{
0:2
4:1
8:1
}

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numCount = {0:1}
        prefix = 0
        res = 0
        for num in nums:
            prefix+=num
            if prefix-k in numCount:
                res+=numCount[prefix-k]
            numCount[prefix] = 1 + numCount.get(prefix, 0)

        return res

        