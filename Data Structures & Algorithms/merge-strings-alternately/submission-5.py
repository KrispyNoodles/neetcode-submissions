class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        answer = ""

        # check which is longer
        for i in range(min(len(word1), len(word2))):
            answer+=word1[i]
            answer+=word2[i]

        
        if i<len(word1)-1:
            answer+=word1[i+1:len(word1)]

        if i<len(word2)-1:
            answer+=word2[i+1:len(word2)]

        return answer