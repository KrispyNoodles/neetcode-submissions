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

        print(int_dict)

        # sorting the dict based on the values
        # lambda helps to use the item's value as the key to be 
        # sorted by most appearance to least
        sorted_pairs = sorted(int_dict.items(), key=lambda x:x[1], reverse=True)

        print(sorted_pairs)

        # answer
        ans_array = []


        # as long as the length is within, append
        for value, appearance in sorted_pairs:
            if len(ans_array) < k:
                ans_array.append(value) 
            else:
                break

        return ans_array
        
        