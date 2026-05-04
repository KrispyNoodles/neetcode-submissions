import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # sort the points based on a calculaiton of the eucildean of each point to the origin
        points.sort(key=lambda x: math.sqrt(x[0]*x[0]+x[1]*x[1]))

        return points[:k]
        