class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        charCount = {}
        for num in nums:
            charCount[num] = charCount.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in charCount.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        
        return res
