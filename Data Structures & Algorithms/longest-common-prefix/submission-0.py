class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        answer = ""
        for i in range(len(strs[0])):

            for word in strs:
                if strs[0][0:i+1] == word[0:i+1]:
                    continue            
                else:
                    return strs[0][0:i]


        # if after everything it suceed then return the whole word
        return strs[0]