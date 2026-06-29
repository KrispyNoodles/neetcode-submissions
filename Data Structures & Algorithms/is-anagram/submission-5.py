class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # creating 2 maps
        map_1 = {}

        for char in s:
            if char not in map_1:
                map_1[char] = 1
            else:
                map_1[char] += 1
        
        map_2 = {}
        for char in t:
            if char not in map_2:
                map_2[char] = 1
            else:
                map_2[char] += 1

        if map_1 == map_2:
            return True

        else:
            return False