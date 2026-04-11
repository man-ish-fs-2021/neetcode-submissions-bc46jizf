class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def func(li, start, end):
            dp = [-1] * n
            def helper(li, start, end):
                if start > end:
                    return 0
                if dp[start] != -1:
                    return dp[start]
                else:
                    dp[start] = max(helper(nums, start + 1, end), nums[start] +  helper(nums, start + 2, end)) 
                return dp[start]
            return helper(li, start, end)
            

        return max(func(nums, 0, n-2), func(nums, 1, n-1))