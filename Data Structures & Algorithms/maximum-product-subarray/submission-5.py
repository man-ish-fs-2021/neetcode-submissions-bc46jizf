class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        op = nums[0]
        currMax = 1
        currMin = 1
        for num in nums:
            tmp = currMax * num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(tmp, num*currMin, num)
            op = max(currMax, op)
        return op 


        