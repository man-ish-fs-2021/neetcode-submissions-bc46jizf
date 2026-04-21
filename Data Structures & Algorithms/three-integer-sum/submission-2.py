class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        for i,a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threesum = a + nums[j] + nums[k] 
                if threesum > 0:
                    k -=1
                elif threesum < 0:
                    j += 1
                else:
                    op.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return op
        