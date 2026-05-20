from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr_prefix = 0
        counter = 0

        # 0 refers that the sum of 0 appeared once before, and 1 refers to the number of times it has appeared
        prefix_count = {0:1}

        # k == s_j-s_i-1
        # reaarange to s_i-1 == s_j-k 
        
        # need = prefix_sum-k
        for val in nums:
            
            # generating curr_prefix
            curr_prefix+=val

            need = curr_prefix-k
            
            # (current prefix-k) has this be seen before?
            if need in prefix_count:
                
                # add how many times 'need' has appeareed before to the counter
                counter+=prefix_count[need]

            # add the current prefix in
            # if exist, increment, else create
            if curr_prefix in prefix_count:
                prefix_count[curr_prefix] += 1
            
            else:
                prefix_count[curr_prefix] = 1

        return counter

# time complexity of O(n)