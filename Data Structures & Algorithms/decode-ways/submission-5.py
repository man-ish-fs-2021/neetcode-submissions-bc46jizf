class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1]*(len(s) + 1)
        def helper(i):

            if i == len(s):
                return 1
            if dp[i] != -1:
                return dp[i]
            if s[i] == '0':
                return 0
            op = helper(i+1)
            # this is in case 2 digits form a valid number
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    op += helper(i+2)
            dp[i] = op
            return op
        return helper(0)