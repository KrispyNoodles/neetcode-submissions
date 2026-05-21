class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        answer = ""
        for i in range(len(strs[0])):

            for word in strs:
                if i>len(word)-1 or strs[0][i] != word[i]:
                    return strs[0][:i] 

        # if after everything it suceed then return the whole word
        return strs[0]

# time complexity of O(n*m^2) where m is the first string length