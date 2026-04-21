class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can use an object to trakc
        # while printing them, might have to do it in another loop,
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        op =[]
        for i in range(k):
            op.append(heapq.heappop(heap)[1])
        return op