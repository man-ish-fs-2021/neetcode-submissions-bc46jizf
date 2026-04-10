class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newnums = [-num for num in nums]
        heapq.heapify(newnums)
        while k > 1:
            heapq.heappop(newnums)
            k -= 1
        return -newnums[0]

        