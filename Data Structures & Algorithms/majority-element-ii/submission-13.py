class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = {}
        for num in nums:
            if len(res) <= 2:
                res[num] = res.get(num, 0) + 1
                print(res)
            else:
                new_res = {}
                for num, count in res.items():
                    if count > 1:
                        new_res[num] = count - 1
                res = new_res
            
        ans = []
        for num in res:
            if nums.count(num) > len(nums) // 3:
                ans.append(num)
        
        return ans
            
