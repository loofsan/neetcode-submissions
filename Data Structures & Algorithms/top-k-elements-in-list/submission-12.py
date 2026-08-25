class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elems = {}
        for num in nums:
            elems[num] = elems.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)] 
        for num, count in elems.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)
            
        return res
