from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # creating a dict to store each anagram's index
        # {anagram_1: index_1, index_2 ....}

        # a default dict that stores an list which contains the index of each string
        # this auto creates a key if it is not found in the dict
        anagram_dict = defaultdict(list)

        for index in range(len(strs)):

            # sort the string by sorting
            sorted_string = sorted(strs[index])

            # converting the string into an string that is able to be used as a key
            sorted_string = "".join(sorted_string)

            # add the index to the dict
            anagram_dict[sorted_string].append(index)

        final_ans = []

        # wrtiign the final answer
        for group_index in anagram_dict.values():

            temp_arr = []

            for index in group_index:
                temp_arr.append(strs[index])
            
            final_ans.append(temp_arr)

        return final_ans