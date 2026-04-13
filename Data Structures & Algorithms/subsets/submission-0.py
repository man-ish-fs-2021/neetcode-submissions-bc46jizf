class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        op = []
        def helper(i, curr):
            if i == n:
                op.append(curr[:])
                return
            ele = nums[i]
            curr.append(ele)
            helper(i+1, curr)
            curr.pop()
            helper(i+1, curr)
        helper(0, [])
        return op
        
        