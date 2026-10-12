class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for index in range(len(haystack)-len(needle)+1):

            # if first char match check all
            if haystack[index] == needle[0]:
                 # check if the words are the same
                 if haystack[index:index+len(needle)] == needle:
                    return index

        return -1