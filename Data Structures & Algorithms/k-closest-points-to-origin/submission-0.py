from typing import List
from collections import defaultdict
from math import sqrt

class Solution:
    # k contains how many nearest points needed
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # dict to store the points, and calculation of distance
        new_dict = defaultdict()

        for a,b in points:
            # calcalation
            calc = sqrt(a*a+b*b)
            new_dict[(a,b)] = calc

        # reorder by points
        new_dict = sorted(new_dict.items(), key=lambda x:x[1])

        answer = []

        for values, calc in new_dict:
            formatted_correctly = [values[0], values[1]]
            answer.append(formatted_correctly)

        return answer[:k]

