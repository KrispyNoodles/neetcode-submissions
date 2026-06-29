import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        new_heap = []
        
        # converting stones into the heap
        for s in stones:
            heapq.heappush(new_heap, -s)

        while len(new_heap) > 1:

            pop_1 = heapq.heappop(new_heap)
            pop_2 = heapq.heappop(new_heap)

            # if both stones same, byebye
            if pop_1==pop_2:
                continue

            if pop_2>pop_1:
                new_heap.append(pop_1-pop_2)

            if pop_1>pop_2:
                new_heap.append(pop_2-pop_1)

        if new_heap == []:
            return 0
        else:
            return -new_heap[0]