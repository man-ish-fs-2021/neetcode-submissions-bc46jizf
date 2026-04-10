class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, ele  in enumerate(nums):
            d[ele] = index
        for index, ele  in enumerate(nums):
            diff = target - ele
            if diff in d and d[diff] != index:
                return [index, d[diff]]
        return []
        