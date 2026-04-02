from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # k refers to how many needed
        new_dict = defaultdict(int)

        # creating a dict for each appearance
        for values in nums:
            new_dict[values] +=1

        # sorting the dictionary
        new_dict = sorted(new_dict.items(), key=lambda x:x[1], reverse=True)
        new_dict = dict(new_dict)

        # the answer
        ans_arr = []
        
        for key, value in new_dict.items():
            ans_arr.append(key)
            if len(ans_arr) == k:
                return ans_arr