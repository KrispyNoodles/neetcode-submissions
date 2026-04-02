from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # creating a dict for each value
        # it maps the value to the count of it's appearance
        int_dict = defaultdict(int)

        # looping through and mapping them
        for value in nums:

            # increment whenever it appears
            int_dict[value] +=1

        # sorting the dict based on the values
        # lambda helps to use the item's value as the key to be 
        # sorted by most appearance to least
        sorted_pairs = sorted(int_dict.items(), key=lambda x:x[1], reverse=True)

        # answer
        ans_array = []

        # as long as the length is within, append
        for value, appearance in sorted_pairs:
            if len(ans_array) < k:
                ans_array.append(value) 
            else:
                break

        return ans_array
        
# time complexity is O(nlog(n))
# O(n) comes from looping through all the values in the array
# however O(nlog(n)) comes from sorting the pairs and putting them back into the dictionary

# space complexity is O(n)
# because as the input gets larger the space being used is larger too as well?
        