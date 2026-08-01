class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-s for s in stones]
        heapq.heapify(min_heap)

        while len(min_heap) != 1:
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap)

            heapq.heappush(min_heap, -abs(x - y))

        return -min_heap[0]