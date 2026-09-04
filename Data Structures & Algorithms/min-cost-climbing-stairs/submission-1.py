class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def dfs(floor):
            if floor >= len(cost):
                return 0
            
            if floor in memo:
                return memo[floor]
            
            memo[floor] = cost[floor] + min(dfs(floor+1), dfs(floor+2))
            return memo[floor]
                
        return min(dfs(0), dfs(1))
            
