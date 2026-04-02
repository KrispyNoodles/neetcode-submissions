from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # creating a dict 
        # string: counter

        # empty map
        # if you try to acces a value that does exist it creates for you
        # the list is what is the datatype of the values
        set_map = defaultdict(list)

        for string in strs:

            # reordering the string
            sort = sorted(string)
            sort = "".join(sort)

            # append the string based on it's alphabetically sorted characters
            set_map[sort].append(string)
            
        return [i for i in set_map.values()]