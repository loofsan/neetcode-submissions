class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in res.items():
            buckets[count].append(num)
        
        count = 0
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if count == k:
                    return ans
                
                ans.append(num)
                count += 1
        
        return ans
                