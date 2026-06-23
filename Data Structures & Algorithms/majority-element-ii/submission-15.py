class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nmap = {}

        for num in nums:
            if len(nmap) != 3:
                nmap[num] = nmap.get(num, 0) + 1
            tempMap = {}
            for num in nmap:
                if nmap[num] > 1:
                    tempMap[num] = nmap[num] - 1

        res = []
        for num in nmap.keys():
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        
        return res