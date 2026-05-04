class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if different len return false
        if len(s) != len(t):
            return False
        
        # create 2 map
        map_1 = {}
        map_2 = {}

        for i in range(len(s)):
            if s[i] not in map_1:
                map_1[s[i]]=1
            else:
                map_1[s[i]]+=1

            if t[i] not in map_2:
                map_2[t[i]]=1
            else:
                map_2[t[i]]+=1

        return map_1==map_2