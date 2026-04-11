class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(li):
            if not li:
                return 0
            if len(li) == 1:
                return li[0]
            dp = [0] * len(li)
            dp[0] = li[0]
            dp[1] = max(li[0], li[1])
            for i in range(2, len(li)):
                dp[i] = max(dp[i-1], li[i]+dp[i-2]) 
            return dp[-1 ]
        return max(helper(nums[1:]), helper(nums[:-1]))

