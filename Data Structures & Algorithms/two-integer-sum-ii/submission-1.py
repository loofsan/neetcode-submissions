class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        right = -1
        left = 0

        for i in range(len(numbers)):
            if numbers[i] > target:
                right = i - 1
        
        right = len(numbers) - 1
        
        while right > left:
            if numbers[right] + numbers[left] == target:
                return [left+1, right+1]
            elif numbers[right] + numbers[left] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1

        