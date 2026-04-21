class Solution:
    # brute force
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        arrl = [0]*n
        arrr = [0]*n
        arrl[0] = 1
        arrr[n-1] = 1
        for i in range(1, n):
            arrl[i] = arrl[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            arrr[i] = arrr[i+1] * nums[i+1]
        for i in range(n):
            res[i] = arrl[i] * arrr[i]
        return res
        