class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for index, char in enumerate(s):

            temp_set = list(s)
            temp_set.remove(char)
            temp_set = set(temp_set)

            if char not in temp_set:
                return index

        return -1