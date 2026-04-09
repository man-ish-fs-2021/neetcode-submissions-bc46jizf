# can we recursively check from i, i + 2
# if starting at i, need to decide if i+1 is better or i + i+2 is better,
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)
        def func(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(func(i+1), nums[i] + func(i+2))
            return dp[i]
        return func(0)

        