class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        heap=[]
        for stone in stones:
            heap.append(-stone)

        heapq.heapify(heap)

        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)

            if y!=x:
                y=y-x
                heapq.heappush(heap,-y)

        if heap:
            return -heap[0]
        return 0
        


        