class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxHeightLeft, maxHeightRight = 0, 0
        l, r = 0, len(height) - 1
        totalWater = 0
        while l < r:
            maxHeightLeft = max(height[l], maxHeightLeft)
            maxHeightRight = max(height[r], maxHeightRight)

            if height[l] < min(maxHeightLeft, maxHeightRight):
                totalWater += maxHeightLeft - height[l]
            if height[r] < min(maxHeightLeft, maxHeightRight):
                totalWater += maxHeightRight - height[r]
            
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return totalWater