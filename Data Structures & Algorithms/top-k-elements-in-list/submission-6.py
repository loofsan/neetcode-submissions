class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        countArr = [[] for _ in range(len(nums) + 1)]

        for num, count in num_count.items():
            countArr[count].append(num)
 
        count = 0
        res = []
        for i in range(len(countArr) - 1, -1, -1):
            for num in countArr[i]:
                if count == k:
                    return res
                else:
                    res.append(num)
                    count += 1

        return res