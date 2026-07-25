"""
- We establish l ptr and r ptr at the ends of the array
- we have  minMaxHeight to hold rainwater
    - this is going to be the min heights of the two walls
- we establish result array (res)

- while l < r:
    - if the min height of the two pointers are taller than the minMaxHeight,
        - we update minMaxHeight

    height1 = minMaxHeight - height[l]
    height2 = minMaxHeight - height[r]

    if height1 > 0:
        res += height1
    if height2 > 0:
        res += height2

    if height[l] <= height[r]:
        l += 1
    elif height[l] > height[r]:
        r -= 1

height = [0, 7, 1, 4, 6]
l = 1
r = 2
minMaxHeight = 6
res = 7
height1 = -1
height2 = 5


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        minMaxHeight = 0
        res = 0

        while l < r:
            minMaxHeight = max(minMaxHeight, min(height[l], height[r]))

            heightL = minMaxHeight - height[l]
            heightR = minMaxHeight - height[r]

            if heightL > 0:
                res += heightL
            if heightR > 0:
                res += heightR

            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return res
