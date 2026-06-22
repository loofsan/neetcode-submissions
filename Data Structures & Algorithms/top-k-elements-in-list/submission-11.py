class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in countMap.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res
