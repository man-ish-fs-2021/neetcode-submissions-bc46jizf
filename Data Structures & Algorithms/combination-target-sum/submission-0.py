class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # this is like the coins sum
        n = len(nums)
        op = []
        def helper(i, curr, total):
            if total > target:
                return 
            if total == target:
                op.append(curr[:])
                return
            if i >= n:
                return
            # for combinations, we should loop with the entire input array to get all possible combinations
            for j in range(i, n):
                ele = nums[j]
                curr.append(ele)
                helper(j, curr, total + ele)
                curr.pop()
            return
        helper(0, [], 0)
        return op
        