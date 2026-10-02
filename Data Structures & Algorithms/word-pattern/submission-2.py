class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # creating a map
        m = {}
        
        i = 0
        s_split = s.split()

        if len(pattern)!=len(s_split):
            return False
        
        for word in s_split:
            if word not in m:
                # checking if the pattern is in the dict
                if pattern[i] in m.values():
                    return False
                m[word]=pattern[i]
            else:
                # check if they match
                if m[word]!=pattern[i]:
                    return False

            i+=1
        return True

