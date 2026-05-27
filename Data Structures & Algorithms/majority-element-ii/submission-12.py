class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            
            count[num] += 1

            if len(count) <= 2:
                continue
            
            new_count = defaultdict(int)
            for n, c in count.items():
                if count[n] > 1:
                    new_count[n] = c - 1
            
            count = new_count
        print(count)
        res = []
        for n in count.keys():
            rc = nums.count(n)
            if rc > len(nums) // 3:
                res.append(n)

        return res
            


