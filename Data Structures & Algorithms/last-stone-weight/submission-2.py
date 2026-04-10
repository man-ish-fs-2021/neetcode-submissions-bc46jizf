# 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap= [-stone for stone in stones ]
        heapq.heapify(stoneHeap)
        print(stoneHeap)

        while len(stoneHeap) > 1:
            first = heapq.heappop(stoneHeap)
            second = heapq.heappop(stoneHeap)
            diff = abs(first-second)
            heapq.heappush(stoneHeap, -diff);
        print(stoneHeap)
        stoneHeap.append(0)
        return abs(stoneHeap[0])
        