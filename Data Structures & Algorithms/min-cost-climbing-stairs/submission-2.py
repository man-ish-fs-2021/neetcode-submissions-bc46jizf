class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost) + 2)
        def func(c, step):
            if step >= len(c):
                return 0
            ans1,ans2 = 1000000, 1000000
            if dp[step+1] != -1:
                ans1 = dp[step+1]
            else:
                ans1 = func(c, step + 1)
            if dp[step+2] != -1:
                ans2 = dp[step+2]
            else:
                ans2 = func(c, step + 2)
            dp[step] = c[step] + min(ans1, ans2)
            return dp[step]
        return min(func(cost, 1), func(cost, 0))

        