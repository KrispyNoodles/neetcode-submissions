import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        new_points = []

        # calculating the eculdian distance of each point
        for point in points:
            ecu_cal = point[0]*point[0] + point[1]*point[1] 
            new_points.append((ecu_cal, point))

        # creating a heap, 
        heapq.heapify(new_points)

        # answer
        answer = []

        # add in the answer based of k
        # since the smallest is what is being pop
        while len(answer)<k:
            temp = heapq.heappop(new_points)

            # append only the points
            answer.append(temp[1])

        return answer
