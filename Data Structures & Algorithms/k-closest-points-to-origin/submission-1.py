# heap approach
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1,x2,y1,y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        # should put the distances in a heap?
        # how will we track the points with the distances?
        origin = [0,0]
        minHeap = [(distance(origin[0], point[0], origin[1], point[1]), [point[0], point[1]]) for point in points]
        print(minHeap)
        heapq.heapify(minHeap)
        print(minHeap)
        op = []
        while k > 0:
            dist, [x, y] = heapq.heappop(minHeap)
            op.append([x,y])
            k -= 1
        return op

        