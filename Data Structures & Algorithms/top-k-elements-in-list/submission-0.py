class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can use an object to trakc
        # while printing them, might have to do it in another loop,
        if not nums:
            return []
        res = {}

        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1
        sorted_items = sorted(res.items(), key=lambda x: x[1])
        count = k
        op = []
        while count != 0:
            key, value = sorted_items.pop()
            op.append(key)
            count -= 1
        return op