class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        state = set(nums)
        for num in nums:
            curr = num
            temp = 0
            while curr in state:
                temp += 1
                curr += 1
            res = max(res, temp)
        return res