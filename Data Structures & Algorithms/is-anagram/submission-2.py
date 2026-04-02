# alternative method of Hash Map

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if length different reutn False, it defo wont match
        if len(s) != len(t):
            return False
        
        # creating a dict for each and checking if they are the same
        dict_s = {}
        dict_t = {}

        # it does the check infront so it can just do the assigning here
        for index in range(len(s)):

            # creating a map for each value, resort to 0 if there is none found
            dict_s[s[index]] = 1 + dict_s.get(s[index], 0)
            dict_t[t[index]] = 1 + dict_t.get(t[index], 0)

        # checking for values and length to be the same
        # this doenst work as 'aaab' is not the same as 'aabb'
        if dict_s == dict_t:
            return True

        else:
            return False
        
# where n is the first string and m is the second
# Time complexity of algo takes O(n+m) since it needs to sort everything by going through all the elemtns

# a much more efficinet way to store