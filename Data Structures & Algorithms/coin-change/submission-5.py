# looks like a take/skip application here
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # take dp of length amount + 1, since we can have any number of combination
        # this can be taken as a recursive knapsack
        dp = [amount + 1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
            


        