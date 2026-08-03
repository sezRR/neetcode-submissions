class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = [-tf for tf in Counter(tasks).values()]
        heapq.heapify(max_heap)

        q = deque()

        t = 0
        while max_heap or q:
            t += 1
            if max_heap:
                task = 1 + heapq.heappop(max_heap)
                if task:
                    q.append((task, t + n))

            if q and q[0][1] == t:
                task, _ = q.popleft()
                heapq.heappush(max_heap, task)
        
        return t



