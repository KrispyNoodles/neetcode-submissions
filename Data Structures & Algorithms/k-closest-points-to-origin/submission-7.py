import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        new_points = []

        # finding which is closest
        for x1,y1 in points:

            calc = (math.sqrt((x1)**2 + (y1)**2))
            new_points.append([calc, (x1,y1)])
        
        # converting it into a heap
        heapq.heapify(new_points)

        answer = []

        while k>0:
            pop_val = heapq.heappop(new_points)
            answer.append(pop_val[1])
            k-=1
        
        return answer