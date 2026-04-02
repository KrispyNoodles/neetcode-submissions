class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # creating a dict for each and checking if they are the same
        dict_s = {}
        dict_t = {}
        
        for value in s:
            # checking if it exists
            if value in dict_s:
                # if does increment it
                dict_s[value] +=1
            else:
                # initalise to be value of 1
                dict_s[value] = 1

        # repeat for t
        for value in t:
            # checking if it exists
            if value in dict_t:
                # if does increment it
                dict_t[value] +=1
            else:
                # initalise to be value of 1
                dict_t[value] = 1
                
        # checking for values and length to be the same
        # this doenst work as 'aaab' is not the same as 'aabb'
        if dict_s == dict_t:
            return True

        else:
            return False
