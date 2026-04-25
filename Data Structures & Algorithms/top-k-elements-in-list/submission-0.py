class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in countMap.items():
            bucket[count].append(num)
        
        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
