class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numsLen = len(nums)
        dp = [-1] * (numsLen+1)
        def lis(li, i, n):
            if i == n:
                return 0,0
            including = 1
            for j in range(i+1, n):
                if li[j]>li[i]:
                    if dp[j] != -1:
                        further = dp[j][0]
                    else:
                        dp[j] = lis(li, j, n)
                        further = dp[j][0]
                    including = max(including, 1 + further)
            if dp[i+1] != -1:
                excluding = dp[i+1][1]
            else:
                dp[i+1] = lis(li, i +1,n)
                excluding = dp[i+1][1]
            overall = max(including, excluding)
            return including, overall
        return lis(nums, 0, numsLen)[1]