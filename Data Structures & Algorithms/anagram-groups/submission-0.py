from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # creating a dict 
        # string: counter

        # empty map
        set_map = {}

        for index in range(len(strs)):

            # sort them first
            string = sorted(strs[index])
            string = "".join(string)
            
            # if it exist increment add the index in
            if string in set_map:
                set_map[string].append(index)
                set_map[string] = set_map[string]

            # empty 
            # create a new dict with its own index
            else:
                set_map[string] = [index]

        # returning the final array
        final_arr = []
        for values in set_map.values():
            temp_arr = []          

            # appending each into the arr
            for indexes in values:
                temp_arr.append(strs[indexes])
                
            final_arr.append(temp_arr)
        
        return final_arr
