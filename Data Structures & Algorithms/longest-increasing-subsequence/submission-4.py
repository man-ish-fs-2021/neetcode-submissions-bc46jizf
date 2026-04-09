class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)]for j in range(n+1)]

        for i in range(n-1, -1, -1):
            including = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    including = max(including, 1 + dp[j][0])
            dp[i][0] = including
            excluding = dp[i+1][1]
            overall = max(including, excluding)
            dp[i][1] = overall
        return dp[0][1]

        