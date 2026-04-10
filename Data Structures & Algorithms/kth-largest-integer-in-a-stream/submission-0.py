class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k;
        self.op = nums
        heapq.heapify(self.op)
        while len(self.op) >  k:
            heapq.heappop(self.op)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.op, val)
        while len(self.op) >  self.k:
            heapq.heappop(self.op)
        return self.op[0]
        
