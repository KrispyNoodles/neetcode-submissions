import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # convert every stones into negative, this way the max value will be the smallest
        # as I am using heapq which is a min-heap

        new_stones = []

        for stone in stones:
            new_stones.append(stone*-1)

        # convert the stones into a heap
        heapq.heapify(new_stones)

        while len(new_stones)>1:

            # pop the first two and then see if need add
            rock_1 = heapq.heappop(new_stones)
            rock_2 = heapq.heappop(new_stones)

            # if rock same, then nothing happens
            if rock_1==rock_2:
                print('both rock same')
            
            # if either rock is bigger then destroy the smaller one
            if rock_1>rock_2:
                heapq.heappush(new_stones, -(rock_1-rock_2))

            if rock_2>rock_1:
                heapq.heappush(new_stones, -(rock_2-rock_1))

            print(new_stones)
        
        # if there are no stones reamining
        if new_stones == []:
            return 0
        
        return abs(new_stones[0])